import setuptools

setuptools.setup(
    name="extension_openvoice",
    packages=setuptools.find_namespace_packages(),
    version="0.0.1",
    author="rsxdalv",
    description="OpenVoice: A versatile instant voice cloning approach",
    url="https://github.com/rsxdalv/extension_openvoice",
    project_urls={},
    scripts=[],
    install_requires=[
        "MyShell-OpenVoice @ git+https://github.com/rsxdalv/OpenVoice@stable",
        # "langid",
        # "numpy",
        # "torch>=2.0.0",
        # "soundfile",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
