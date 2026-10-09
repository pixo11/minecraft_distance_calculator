import os, sys, webview

def resource(name):
    base = getattr(sys, "_MEIPASS", os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base, name)

if __name__ == "__main__":
    webview.create_window(
        "Minecraft Distance Calculator",
        resource("minecraft_distance_calculator.html"),
        width=1100, height=800, min_size=(700, 500),
    )
    # private_mode=False + storage_path keeps localStorage between launches
    webview.start(private_mode=False,
                  storage_path=os.path.join(os.environ.get("APPDATA", "."), "MinecraftDistanceCalculator"))
