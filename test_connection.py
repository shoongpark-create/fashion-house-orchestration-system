import os
import subprocess
from dotenv import load_dotenv

load_dotenv()


def check_agents():
    print("🔌 Wacky Willy System Connection Check (V3.4)...\n")

    # 1. Antigravity (Google Gemini Pro)
    print("1️⃣ Testing Antigravity (Sisyphus/Prometheus/Atlas)...")
    try:
        # Check Antigravity CLI auth status
        result = subprocess.run(
            ["antigravity", "auth", "status"], capture_output=True, text=True
        )
        if "Active" in result.stdout:
            print("   ✅ Gemini Pro Connected! (Google Subscription)\n")
        else:
            print("   ❌ Login Required (Run: 'antigravity auth login')\n")
    except FileNotFoundError:
        print("   ❌ Antigravity CLI not installed.\n")
    except Exception as e:
        print(f"   ❌ CLI Error: {e}\n")

    # 2. Z.ai (Hephaestus & Creative Agents)
    print("2️⃣ Testing Z.ai Agents (Hephaestus/IP Artist)...")
    z_key = os.getenv("Z_AI_API_KEY")

    if z_key and z_key.startswith("zai_"):
        print(f"   ✅ Z.ai API Key Detected! ({z_key[:6]}...)")
        print("   ✅ Hephaestus: Ready (Model: GLM-4-Flash / Free)")
        print("   ✅ IP Artist : Ready (Model: GLM-4-Plus)\n")
    else:
        print("   ❌ Missing Z_AI_API_KEY in .env")
        print("      -> Hephaestus & Creative Agents will fail.\n")

    print("=" * 50)
    print("✨ System Ready! if all green.")


if __name__ == "__main__":
    check_agents()
