[![Open In Colab](https://img.shields.io/badge/Colab-F9AB00?style=for-the-badge&logo=googlecolab&color=525252)](https://colab.research.google.com/drive/1r4IRL0UA7JEoZ0ZK8PKfMyTIBHKpyhcw)

# Local Installation
If you already have RVC installed, then just download GUI.py and drop it in the root folder!
If you need to install RVC, I recommend you check the [original repo](https://github.com/RVC-Project/Retrieval-based-Voice-Conversion-WebUI)
Or read this at least.

I recommend you use a virtual environment

```bash
python -m venv RVC
cd RVC
git clone https://github.com/RVC-Project/Retrieval-based-Voice-Conversion-WebUI
Scripts/activate.bat
pip install torch torchvision torchaudio
cd RVC-Project
wget "https://raw.githubusercontent.com/luisesantillan/project/main/GUI.py"
wget "https://raw.githubusercontent.com/luisesantillan/project/main/download_files.py"
pip install -r "requirements.txt"
```
If you're on Windows, like me, and don't have an NVIDA graphics card, install the requirements from a different .txt:
```bash
pip install -r "requirements-dml.txt"
```
Also, do not forget to download the necessary models. EasyGUI uses RVC 2 40k models.

```bash
python download_files.py
```
Finally, run the demo.py
```bash
python demo.py
```
