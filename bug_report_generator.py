# 🐞 Bug Report Generator — CLI-инструмент для создания Markdown-багов

title = input(" Название бага: ")
steps = input(" Шаги для воспроизведения (через \\n): ")
expected = input("✅ Ожидаемый результат: ")
actual = input("❌ Фактический результат: ")
env = input(" Окружение (устройство, ОС, браузер): ")

filename = title.lower().replace(" ", "_") + ".md"

with open(filename, "w") as f:
    f.write(f"# 🐞 {title}\n\n")
    f.write(f"**Шаги для воспроизведения:**\n{steps}\n\n")
    f.write(f"**Ожидаемый результат:**\n{expected}\n\n")
    f.write(f"**Фактический результат:**\n{actual}\n\n")
    f.write(f"**Окружение:**\n{env}\n")
