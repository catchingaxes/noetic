# See here for image contents: https://github.com/microsoft/vscode-dev-containers/tree/v0.177.0/containers/codespaces-linux/.devcontainer/base.Dockerfile

FROM mcr.microsoft.com/vscode/devcontainers/universal:1-focal

USER root

# RUN apt-get update && export DEBIAN_FRONTEND=noninteractive \
#     && apt-get -y install --no-install-recommends <your-package-list-here>

RUN wget https://get.please.build -O please-install.sh \
    && chmod +x ./please-install.sh

RUN su codespace -c "./please-install.sh"

USER codespace

RUN npm i -g standard commitizen cz-conventional-changelog @microsoft/rush
