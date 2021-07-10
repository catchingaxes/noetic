# See here for image contents: https://github.com/microsoft/vscode-dev-containers/tree/v0.177.0/containers/codespaces-linux/.devcontainer/base.Dockerfile

FROM mcr.microsoft.com/vscode/devcontainers/universal:1-focal

USER root

# RUN apt-get update && export DEBIAN_FRONTEND=noninteractive \
#     && apt-get -y install --no-install-recommends <your-package-list-here>

RUN curl https://get.please.build | bash \
    && source <(plz --completion_script)

USER codespace
