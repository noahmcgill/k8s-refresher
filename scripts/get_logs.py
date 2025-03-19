import asyncio
from kubernetes_asyncio import client, config
from kubernetes_asyncio.client.api_client import ApiClient

async def pull_logs():
    await config.load_kube_config()

    async with ApiClient() as api:
        v1 = client.CoreV1Api(api)

        thread = await v1.read_namespaced_pod_log("api-deployment-697fff58fb-2nqq6", "default")

        print(thread)

if __name__ == "__main__":
    asyncio.run(pull_logs())
