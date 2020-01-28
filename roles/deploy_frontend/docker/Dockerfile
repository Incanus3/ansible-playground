# syntax=docker/dockerfile:1.0.0-experimental

ARG runtime_version=12

FROM node:${runtime_version}-alpine AS build-stage

ARG repo_url
ARG project_branch=master
ARG project_ref=HEAD

RUN apk add --no-cache git openssh-client
RUN npm install -g yarn

RUN mkdir -p -m 0600 ~/.ssh && ssh-keyscan gitlab.alto-apps.mine.nu >> ~/.ssh/known_hosts

RUN --mount=type=ssh git clone --single-branch --no-tags --branch "$project_branch" \
	--separate-git-dir=/tmp/git-dir "$repo_url" /deploy
WORKDIR /deploy
RUN git checkout "$project_ref"

RUN --mount=type=ssh yarn install

ARG env_prefix
ARG frontend_url
ARG backend_url

ENV ${env_prefix}_FRONTEND_URL=${frontend_url}
ENV ${env_prefix}_BACKEND_URL=${backend_url}

COPY entrypoint.sh .

ENTRYPOINT ["/bin/sh", "./entrypoint.sh"]
