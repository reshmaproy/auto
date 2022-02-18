import sys
import semantic_version

#v1 -> version of head branch
#v2 -> version of base branch
s1 = sys.argv[1]
s2 = sys.argv[2]

try:
    v1 = semantic_version.Version(s1)
except ValueError:
    print("Incorrect syntex. Please follow Semantic Versioning")

v2 = semantic_version.Version(s2)

valid = semantic_version.Version(s1) > semantic_version.Version(s2)
sys.stdout.write(valid)
sys.exit(0)
 
