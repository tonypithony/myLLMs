# Ollama. Быстрый старт
```bash
ollama ps
ollama ls
ollama rm <model>
```

Можно кстати немного отконфигурировать модель, для этого создаём файл Modelfile  

пишем в него например это  

```
FROM llama3.1
PARAMETER temperature 1
SYSTEM """
Твоя задача на всё отвечать антонимами на русском языке.
"""
```

теперь создадим модель с этими настройками  

```bash
ollama create anti -f Modelfile
```

и запускаем  

```bash
ollama run anti
```
