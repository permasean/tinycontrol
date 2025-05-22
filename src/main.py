from openai import OpenAI
from dotenv import load_dotenv
import os
import pyautogui
import platform

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def main():
    dim = pyautogui.size()
    os_environment = platform.system().lower()
    if "mac" in os_environment or "darwin" in os_environment:
        os_environment = "mac"
    elif "windows" in os_environment:
        os_environment = "windows"
    elif "linux" in os_environment:
        os_environment = "ubuntu"
    else:
        raise ValueError(f"Unsupported OS: {os_environment}")

    print(f"OS environment: {os_environment}")
    print(f"Display size: {dim.width}x{dim.height}")
    return
    response = client.responses.create(
        model="computer-use-preview",
        tools=[{
            "type": "computer_use_preview",
            "display_width": dim.width,
            "display_height": dim.height,
            "environment": os_environment # other possible values: "mac", "windows", "ubuntu"
        }],    
        input=[
            {
            "role": "user",
            "content": [
                {
                "type": "input_text",
                "text": "Check the latest OpenAI news on bing.com."
                }
                # Optional: include a screenshot of the initial state of the environment
                # {
                #     type: "input_image",
                #     image_url: f"data:image/png;base64,{screenshot_base64}"
                # }
            ]
            }
        ],
        reasoning={
            "summary": "concise",
        },
        truncation="auto",
        store=False
    )

    print(response)

if __name__ == "__main__":
    main()
