import os
import subprocess
import sys

# from django.contrib.gis.utils.ogrinspect import ogrinspect
import shapefile

def main():
  desiredSRID = "4326"
  SRIDNamespace = "EPSG"
  simplificationTolerance = "0.0001"

  dataDir = "world/data"
  reprojectedDir = os.path.join(dataDir, "reprojected")
  simplifiedDir = os.path.join(dataDir, "simplified")

  modelsClasses = ""
  modelsFilters = ""
  modelsGeoFilters = ""
  adminModelImports = "from .models import TextSnugget, EmbedSnugget, SnuggetSection, SnuggetSubSection, Infrastructure, InfrastructureGroup, InfrastructureCategory, RecoveryLevels, Location, SiteSettings"
#  adminSiteRegistrations = ""
  modelsSnuggetReturns = ""
  viewsSnuggetMatches = ""
  adminLists = ""
  loadMappings = ""
  loadPaths = ""
  templateMomentSnuggets = ""
  loadImports = ""

  for subdir in [reprojectedDir, simplifiedDir]:
    if not os.path.exists(subdir):
      os.mkdir(subdir)

  for f in os.listdir(dataDir):
    if f[-4:] == ".shp":
      stem = f[:-4].replace(".", "_").replace("-","_")
      print("Opening shapefile:", stem)
      reprojected = reprojectShapefile(f, dataDir, reprojectedDir, SRIDNamespace+":"+desiredSRID)
      simplified = simplifyShapefile(reprojected, simplifiedDir, simplificationTolerance)

      sf = shapefile.Reader(simplified)
      fieldNames = [x[0] for x in sf.fields[1:]]
      print("Found the following fields in the attribute table:")
      print(str(fieldNames).strip("[").strip("]").replace("'",""))
      print("Which would you like to use to look up snuggets by?")
      keyField = False
      while keyField not in fieldNames:
        keyField = input(">> ")

      modelsClasses += modelClassGen(stem, sf, keyField, desiredSRID)
      modelsFilters += "    " + stem + "_filter = models.ForeignKey(" + stem
      modelsFilters += ", related_name='+', on_delete=models.PROTECT, blank=True, null=True)\n"
      modelsGeoFilters += modelsGeoFilterGen(stem, keyField)

      adminModelImports += ", " + stem

      print("")

  # no need to keep repeating the import statement that ogrinspect puts in
  modelsClasses = modelsClasses.replace("from django.contrib.gis.db import models\n\n", "")

  outputGeneratedCode(modelsClasses, "world/models.py", "Insert generated modelsClasses here")
  outputGeneratedCode(modelsFilters, "world/models.py", "Insert generated modelsFilters here")
  outputGeneratedCode(modelsGeoFilters, "world/models.py", "Insert generated modelsGeoFilters here")
  outputGeneratedCode(adminModelImports, "world/admin.py", "Replace the next line with generated adminModelImports", replace=True)
  print("\n")



def reprojectShapefile(f, inputDir, outputDir, srs):
  original = os.path.join(inputDir, f)
  reprojected = os.path.join(outputDir, f)
  if os.path.exists(reprojected):
    print("Skipping reprojection because this file has previously been reprojected.")
  else:
    print("Reprojecting to", srs)
    ogrCmd = [
      "ogr2ogr",
      reprojected,
      original,
      "-t_srs", srs
    ]
    subprocess.call(ogrCmd)
  return reprojected



def simplifyShapefile(original, outputDir, tolerance):
  simplified = os.path.join(outputDir, os.path.basename(original))
  if os.path.exists(simplified):
    print("Skipping simplification because this file has previously been reprojected.")
  else:
    print("Simplifying with tolerance", tolerance)
    ogrCmd = [
      "ogr2ogr",
      simplified,
      original,
      "-simplify", tolerance
    ]
    subprocess.call(ogrCmd)
  return simplified



def modelClassGen(stem, sf, keyField, srs):
  text = "class " + stem + "(models.Model):\n"
  text += "    " + keyField + " = models."
  for field in sf.fields:
    if field[0] == keyField:
      if field[1] == 'C':
        text += "CharField(max_length=" + str(field[2]) + ")\n"
      elif field[1] == 'N':
        if field[3] > 0:
          text += "FloatField()\n"
        else:
          text += "IntegerField()\n"
      else:
        print("Field type unrecognised:")
        print(field)
        exit()
  text += "    geom = models."
  shapeType = 0
  i = 0
  while shapeType == 0:
    shapeType = sf.shapes()[i].shapeType
    i = i + 1
  if shapeType == 5:
    text += "PolygonField(srid=" + srs + ")\n"
  elif shapeType == 25:
    text += "MultiPolygonField(srid=" + srs + ")\n"
  else:
  	print("Geometry field type ", shapeType, "unrecognised")
  	# the list of valid geometry field type codes is at
  	# https://www.esri.com/library/whitepapers/pdfs/shapefile.pdf p4
  	exit()
  text += "    objects = models.GeoManager()\n\n"
  text += "    def __str__(self):\n"
  text += "        return self." + keyField + "\n\n"

  return text



def modelsGeoFilterGen(stem, keyField):
  text = "        qs_" + stem + " = "
  text += stem + ".objects.filter(geom__contains=pnt)\n"
  text += "        " + stem + "_rating = "
  text += "qs_" + stem + ".values.list('" + keyField + "', flat=True)\n"
  text += "        " + stem + "_snuggets = "
  text += "Snugget.objects.filter(" + stem + "_filter__" + keyField + "__exact="
  text += stem + "_rating).select_subclasses()\n\n"
  return text



def outputGeneratedCode(code, destFile, anchor, replace=False):
  print("\n######################################################\n\n\n\n")
  if replace:
  	prompt = "Replace the line after the '" + anchor + "' comment in "
  	prompt += destFile + " with the following code:\n"
  else:
  	prompt = "Insert the following code after the '" + anchor + "' comment in "
  	prompt += destFile + "\n\n"
  print(prompt)
  print(code)



if __name__ == "__main__":
  main()
