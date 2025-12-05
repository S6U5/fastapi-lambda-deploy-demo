# fastapi-lambda-deploy-demo

AWS初心者がLambdaにデプロイするための練習用リポジトリです。

FastAPIで作成するエンドポイントをAPI Gatewayで呼び出せるようにすることが目標です。

## 使用した技術スタック

![AWS Lambda](https://img.shields.io/badge/AWS%20Lambda-%23FF9900.svg?style=for-the-badge&logo=aws-lambda&logoColor=white)
![Amazon API Gateway](https://img.shields.io/badge/API%20Gateway-%235A3E85.svg?style=for-the-badge&logo=amazon-aws&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-009688.svg?style=for-the-badge&logo=FASTAPI&logoColor=white)
![Python](https://img.shields.io/badge/Python%203.12-3776AB.svg?style=for-the-badge&logo=python&logoColor=white)
![Mangum](https://img.shields.io/badge/Mangum-%23009688.svg?style=for-the-badge)
![Serverless Framework](https://img.shields.io/badge/Serverless-%23FD5750.svg?style=for-the-badge&logo=serverless&logoColor=white)
![GitHub Actions](https://img.shields.io/badge/GitHub%20Actions-%232088FF.svg?style=for-the-badge&logo=github-actions&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED.svg?style=for-the-badge&logo=docker&logoColor=white)
![VS Code](https://img.shields.io/badge/VS%20Code-007ACC.svg?style=for-the-badge&logo=visual-studio-code&logoColor=white)


## ToDo
- [ ] DeployにはGitHub Actionsを使用します
- [ ] シークレットキー形式ではなくてOICDを用いてでデプロイをおこなう
- [ ] serverlessを設定する
- [ ] Hello WorldをJsonで出力
- [ ] まずは、EnventBridgeで簡単な呼び出しをできるようにする
- [ ] ローカルのフロントエンドとCORSを設定して呼び出せるように
- [ ] GitHub Actionsと連携する
- [ ] 機密性をそれなり担保する設計を実装する
