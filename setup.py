import setuptools

setuptools.setup(
    name="vscode-proxy",
    version='0.1.0',
    url="https://github.com/ReneNeu/vscode-proxy",
    author="Rene Neuhaus",
    description="Proxy for VS Code to start in Browser",
    packages=setuptools.find_packages(),
	  keywords=['Jupyter', 'Proxy', 'VS Code'],
	  classifiers=['Framework :: Jupyter'],
    install_requires=[
        'jupyter-server-proxy'
    ],
    entry_points={
        'jupyter_serverproxy_servers': [
            'vscode = vscode_proxy:setup_vscode',
        ]
    },
    package_data={
        'vscode_proxy': ['icons/*'],
    },
)
