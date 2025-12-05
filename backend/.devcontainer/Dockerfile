# ステージ1: AWS CLI インストール
FROM python:3.12-slim as aws-installer
RUN apt-get update && \
    apt-get install -y curl unzip && \
    curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip" && \
    unzip awscliv2.zip && \
    ./aws/install --bin-dir /aws-cli-bin/

# ステージ2: メインイメージ
FROM python:3.12-slim

# AWS CLI をコピー
COPY --from=aws-installer /usr/local/aws-cli/ /usr/local/aws-cli/
COPY --from=aws-installer /aws-cli-bin/ /usr/local/bin/

# 必要なパッケージのインストール
RUN apt-get update && \
    apt-get install -y \
    nodejs \
    npm \
    git \
    less \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Serverless Framework のインストール
RUN npm install -g serverless

WORKDIR /workspace

# Python depsは postCreateCommand でインストール
CMD ["/bin/bash"]