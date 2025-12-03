#!/usr/bin/env python3
import sys
import os

# Path to the finder file
finder_file = 'venv_test/lib/python3.13/site-packages/__editable___shade_privacy_1_0_0_finder.py'

print(f"Reading finder file: {finder_file}")
with open(finder_file, 'r') as f:
    content = f.read()

# The MAPPING dictionary should map package names to paths
# Add this after the MAPPING definition
fix_code = '''
MAPPING["shade_privacy"] = "/home/pete/projects/sdks/shade_privacy"
'''

# Find where MAPPING is defined and add our mapping
if 'MAPPING: dict[str, str] = {}' in content:
    # Replace empty dict with our mapping
    new_content = content.replace(
        'MAPPING: dict[str, str] = {}',
        'MAPPING: dict[str, str] = {"shade_privacy": "/home/pete/projects/sdks/shade_privacy"}'
    )
    
    # Write back
    with open(finder_file, 'w') as f:
        f.write(new_content)
    print("✅ Fixed finder file")
    
    # Test it
    print("\nTesting fixed finder...")
    exec(open(finder_file).read())
    
    # Call install
    install()
    
    # Try to find the module
    import importlib.util
    spec = importlib.util.find_spec('shade_privacy')
    print(f"Module spec after fix: {spec}")
    
    if spec:
        print(f"✅ Success! Origin: {spec.origin}")
        
        # Try to load it
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        print(f"✅ Module loaded: {module}")
        print(f"Attributes: {[x for x in dir(module) if not x.startswith('_')]}")
else:
    print("❌ Couldn't find MAPPING definition in finder file")
