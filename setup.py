import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = fh.read().split("\n")


setuptools.setup(
    name="rife",
    version="0.0.1dev0",
    author="Xing Han Lu",
    author_email="github@xinghanlu.com",
    description="A fork of arxiv2020-RIFE with PyPi installation and console scripts",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/xhlulu/rife",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=setuptools.find_packages(),
    python_requires=">=3.6",
    install_requires=requirements,
    entry_points=dict(
        console_scripts=[
            'rife-video=rife.console_scripts.inference_video:main',
            'rife-img=rife.console_scripts.inference_img:main'
        ]
    )
)