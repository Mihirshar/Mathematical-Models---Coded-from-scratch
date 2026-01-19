# Setup Script Documentation

## 📄 About `setup_enhanced_structure.py`

This script automates the creation of a comprehensive, production-ready repository structure for the AI/ML Generative Foundations project.

---

## 🎯 Purpose

The script addresses **23 categories of enhancements** identified through structural analysis, creating:
- Testing infrastructure
- CI/CD pipelines
- Documentation systems
- Code quality tools
- Development workflows
- And much more!

---

## 🚀 Usage

### Basic Usage
```bash
python setup_enhanced_structure.py
```

### With Custom Path
```bash
python setup_enhanced_structure.py --base-path /path/to/repo
```

### Help
```bash
python setup_enhanced_structure.py --help
```

---

## 📦 What It Creates

### Directories (30+)
- `tests/` - Testing infrastructure
- `.github/workflows/` - CI/CD pipelines
- `docs/` - Documentation
- `data/` - Data management
- `notebooks/` - Jupyter notebooks
- `scripts/` - Utility scripts
- `examples/` - Quick-start examples
- `configs/` - Configuration files
- `models/` - Model storage
- `benchmarks/` - Performance tests
- `deployment/` - Deployment templates
- `resources/` - Learning materials
- `src/ml_foundations/` - Python package
- `requirements/` - Granular requirements
- `assets/` - Images & diagrams
- `logs/` - Application logs
- And more...

### Configuration Files (25+)
- `pytest.ini` - Testing configuration
- `.pre-commit-config.yaml` - Git hooks
- `mkdocs.yml` - Documentation
- `.flake8` - Linting
- `.gitattributes` - Git attributes
- `.mailmap` - Contributor mapping
- `Makefile` - Task automation
- `.bandit` - Security scanning
- And more...

### Documentation Files (15+)
- `CODE_OF_CONDUCT.md`
- `SECURITY.md`
- `CHANGELOG.md`
- `AUTHORS.md`
- `FAQ.md`
- `TROUBLESHOOTING.md`
- `SETUP_GUIDE.md`
- `QUICK_START.md`
- `SETUP_CHECKLIST.md`
- And more...

### Template Files (20+)
- GitHub workflow templates
- Issue/PR templates
- Test templates
- Script templates
- Example code
- Configuration templates
- Deployment templates
- And more...

---

## 🔧 How It Works

### Class Structure

```python
class RepositoryEnhancer:
    """Main class that orchestrates the setup."""
    
    def __init__(self, base_path: str = ".")
    def create_directory(self, path: str) -> None
    def create_file(self, path: str, content: str) -> None
    
    # Setup methods (one per enhancement category)
    def setup_testing_infrastructure(self) -> None
    def setup_cicd_pipeline(self) -> None
    def setup_documentation(self) -> None
    # ... and 17 more setup methods
    
    def run_all_setups(self) -> None
```

### Execution Flow

1. **Initialize** - Create RepositoryEnhancer instance
2. **Setup Methods** - Run each setup method sequentially
3. **Create Items** - Create directories and files
4. **Track Progress** - Log all created items
5. **Summary** - Display completion summary

### Safety Features

- **No Overwriting**: Existing files are never overwritten
- **Skip Existing**: Skips files/directories that already exist
- **Error Handling**: Graceful error handling
- **Logging**: Detailed logging of all operations
- **Dry Run Capable**: Can be modified for dry-run mode

---

## 📋 Setup Methods

### 1. `setup_testing_infrastructure()`
Creates complete testing framework with pytest configuration, test directories, sample tests, and fixtures.

### 2. `setup_cicd_pipeline()`
Sets up GitHub Actions workflows, pre-commit hooks, issue templates, and PR templates.

### 3. `setup_documentation()`
Creates MkDocs configuration, documentation structure, and index pages.

### 4. `setup_data_structure()`
Organizes data directories (raw, processed, external, interim) with documentation.

### 5. `setup_notebooks()`
Creates notebook directories organized by topic with naming conventions.

### 6. `setup_scripts()`
Adds utility scripts for data download, environment setup, and training.

### 7. `setup_examples()`
Creates quick-start examples and sample implementations.

### 8. `setup_configs()`
Sets up configuration management with model, training, and data configs.

### 9. `setup_models_structure()`
Organizes model storage directories for pretrained models, checkpoints, and exports.

### 10. `setup_benchmarks()`
Creates benchmarking framework with templates.

### 11. `setup_deployment()`
Adds deployment templates (FastAPI, Kubernetes, serverless).

### 12. `setup_community_files()`
Creates community governance files (CODE_OF_CONDUCT, SECURITY, etc.).

### 13. `setup_additional_docs()`
Adds FAQ, troubleshooting guide, and other documentation.

### 14. `setup_resources()`
Creates learning resources directory with curated lists.

### 15. `setup_package_structure()`
Sets up proper Python package structure with src/ layout.

### 16. `setup_requirements_files()`
Creates granular requirements files for different purposes.

### 17. `setup_code_quality_configs()`
Configures linting, formatting, and type checking tools.

### 18. `setup_git_configs()`
Adds git configuration files (.gitattributes, .mailmap).

### 19. `setup_ide_configs()`
Creates IDE configuration examples (VS Code).

### 20. `setup_makefile()`
Generates Makefile with common development tasks.

### 21. `setup_assets()`
Creates assets directory for images and diagrams.

### 22. `setup_monitoring()`
Sets up logging and monitoring configurations.

### 23. `setup_additional_modules()`
Adds missing curriculum modules (autoencoders, GANs, diffusion models, etc.).

---

## 🎨 Customization

### Modify Existing Setup

Edit any setup method to customize what gets created:

```python
def setup_testing_infrastructure(self):
    # Modify test directories
    test_dirs = [
        "tests",
        "tests/unit",
        "tests/integration",
        "tests/my_custom_tests",  # Add custom directory
    ]
    for dir_path in test_dirs:
        self.create_directory(dir_path)
```

### Add New Setup Method

```python
def setup_my_custom_feature(self):
    """Create my custom feature."""
    print("\n🎯 Setting up My Custom Feature...")
    
    self.create_directory("my_feature")
    
    content = """# My Custom Feature
    
    Description here.
    """
    self.create_file("my_feature/README.md", content)
```

Then add to `run_all_setups()`:

```python
def run_all_setups(self):
    # ... existing setups ...
    self.setup_my_custom_feature()
```

### Skip Certain Setups

Comment out setups you don't need:

```python
def run_all_setups(self):
    self.setup_testing_infrastructure()
    # self.setup_benchmarks()  # Skip benchmarks
    # self.setup_deployment()  # Skip deployment
    self.setup_documentation()
```

---

## 🔍 Output

### Console Output

The script provides detailed console output:

```
============================================================
🚀 ENHANCED REPOSITORY STRUCTURE SETUP
============================================================

🔬 Setting up Testing Infrastructure...
✓ Created directory: tests
✓ Created directory: tests/unit
✓ Created file: pytest.ini
...

✅ SETUP COMPLETE!
============================================================

Total items created: 127

📋 Summary of created items:
  📁 Directories: 35
  📄 Files: 92

🎯 Next Steps:
  1. Review the created structure
  2. Install dependencies: make install-dev
  ...
```

### Tracking

All created items are tracked in `self.created_items` list for reporting.

---

## ⚠️ Important Notes

### Existing Files
- **Never overwrites** existing files
- Skips files that already exist
- Safe to run multiple times

### Permissions
- Requires write permissions in repository
- Creates files with default permissions
- Shell scripts may need `chmod +x`

### Platform Compatibility
- Works on Windows, macOS, Linux
- Uses `pathlib.Path` for cross-platform paths
- Shell scripts are Unix-style (may need adaptation for Windows)

---

## 🐛 Troubleshooting

### Permission Denied
```bash
# Make script executable
chmod +x setup_enhanced_structure.py
```

### Import Errors
```bash
# Ensure you're in the repository root
cd /path/to/repository
python setup_enhanced_structure.py
```

### Path Issues
```bash
# Use absolute path
python setup_enhanced_structure.py --base-path /absolute/path/to/repo
```

### Partial Setup
If script fails midway:
- Already created items are preserved
- Safe to run again
- Will skip existing items and continue

---

## 🧪 Testing the Script

### Dry Run (Manual)
Modify the script to add a dry-run mode:

```python
def __init__(self, base_path: str = ".", dry_run: bool = False):
    self.base_path = Path(base_path)
    self.dry_run = dry_run
    self.created_items = []

def create_directory(self, path: str) -> None:
    if self.dry_run:
        print(f"[DRY RUN] Would create directory: {path}")
        return
    # ... actual creation code ...
```

### Test in Temporary Directory
```python
import tempfile

with tempfile.TemporaryDirectory() as tmpdir:
    enhancer = RepositoryEnhancer(base_path=tmpdir)
    enhancer.run_all_setups()
    # Verify structure
```

---

## 📊 Statistics

### Execution Time
- Typical run: 5-10 seconds
- Depends on disk I/O speed
- Creates 100+ files quickly

### Disk Space
- Minimal: ~1-2 MB
- Mostly text files
- No large binaries

---

## 🔄 Maintenance

### Updating the Script

When adding new enhancements:

1. Create new setup method
2. Add to `run_all_setups()`
3. Test in isolation
4. Update documentation
5. Commit changes

### Version Control

The script itself should be version controlled:
- Track changes in git
- Document major updates in CHANGELOG.md
- Tag versions if needed

---

## 📚 Related Documentation

- `SETUP_GUIDE.md` - Detailed setup instructions
- `QUICK_START.md` - Quick start guide
- `SETUP_CHECKLIST.md` - Setup verification checklist
- `ENHANCEMENTS_SUMMARY.md` - What was enhanced
- `TROUBLESHOOTING.md` - Common issues

---

## 🤝 Contributing

To improve the setup script:

1. Fork the repository
2. Modify `setup_enhanced_structure.py`
3. Test thoroughly
4. Update documentation
5. Submit pull request

---

## 📞 Support

Issues with the setup script?

1. Check `TROUBLESHOOTING.md`
2. Review this documentation
3. Open a GitHub issue
4. Tag with `setup-script` label

---

## 🎉 Success Criteria

The script is successful when:
- ✅ All directories created
- ✅ All files created
- ✅ No errors during execution
- ✅ Repository structure complete
- ✅ Ready for development

---

## 📝 License

This script is part of the AI/ML Generative Foundations repository and follows the same MIT License.

---

**Script Version:** 1.0.0
**Last Updated:** 2024-01-20
**Maintainer:** Mathematical Models Team
