from datetime import datetime

def application():
    message = "Jenkins Multi Pipeline Python Demo"
    print("=" * 50)
    print(message)
    print(f"Execution Time: {datetime.now()}")
    print("=" * 50)

    return True


if __name__ == "__main__":
    application()
