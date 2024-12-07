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

# Llama 3.2 Vision

# Fine Tuning Large Language Model (LLM)

# Bonus: conky (Ubuntu)

conky.conf  

```
-- cat /etc/conky/conky.conf

-- Conky, a system monitor https://github.com/brndnmtthws/conky
--
-- This configuration file is Lua code. You can write code in here, and it will
-- execute when Conky loads. You can use it to generate your own advanced
-- configurations.
--
-- Try this (remove the `--`):
--
--   print("Loading Conky config")
--
-- For more on Lua, see:
-- https://www.lua.org/pil/contents.html

conky.config = {
    alignment = 'top_left',
    background = false,
    border_width = 1,
    cpu_avg_samples = 2,
    default_color = 'white',
    default_outline_color = 'white',
    default_shade_color = 'white',
    double_buffer = true,
    draw_borders = false,
    draw_graph_borders = true,
    draw_outline = false,
    draw_shades = false,
    extra_newline = false,
    font = 'DejaVu Sans Mono:size=12',
    gap_x = 60,
    gap_y = 60,
    minimum_height = 5,
    minimum_width = 5,
    net_avg_samples = 2,
    no_buffers = true,
    out_to_console = false,
    out_to_ncurses = false,
    out_to_stderr = false,
    out_to_x = true,
    own_window = true,
    own_window_class = 'Conky',
    own_window_type = 'desktop',
    show_graph_range = false,
    show_graph_scale = false,
    stippled_borders = 0,
    update_interval = 1.0,
    uppercase = false,
    use_spacer = 'none',
    use_xft = true,
    own_window_transparent = true,
    own_window_argb_visual = true,
}

conky.text = [[
${color grey}Info:$color ${scroll 32 Conky $conky_version - $sysname $nodename $kernel $machine}
${color orange}$hr
${color grey}Uptime:$color $uptime
${color grey}Frequency (in MHz):$color $freq
${color grey}Frequency (in GHz):$color $freq_g
${color grey}RAM Usage:$color $mem/$memmax - $memperc% ${membar 4}
${color grey}Swap Usage:$color $swap/$swapmax - $swapperc% ${swapbar 4}
${color grey}CPU Usage:$color $cpu% ${cpubar 4}
${color grey}Processes:$color $processes  ${color grey}Running:$color $running_processes
${color orange}$hr
${color grey}File systems:
 / $color${fs_used /}/${fs_size /} ${fs_bar 6 /}
${color grey}Networking:
Up:$color ${upspeed} ${color grey} - Down:$color ${downspeed}
${color orange}$hr
${color grey}Name              PID     CPU%   MEM%
${color lightgrey} ${top name 1} ${top pid 1} ${top cpu 1} ${top mem 1}
${color lightgrey} ${top name 2} ${top pid 2} ${top cpu 2} ${top mem 2}
${color lightgrey} ${top name 3} ${top pid 3} ${top cpu 3} ${top mem 3}
-- ${color lightgrey} ${top name 4} ${top pid 4} ${top cpu 4} ${top mem 4}
${color orange}$hr
${color orange}GPU:${exec nvidia-smi -L | cut -c 8-17}
${color orange}Temperature: ${color orange}${exec nvidia-smi -q -d temperature | perl -ne 'print/([0-9]+)/ if /GPU Current Temp/i'} C
${color orange}Used:${exec nvidia-smi -i 0 -q -d MEMORY |grep "Used" | cut -c 45-55 | head -1}
]]
```

# Bonus 2: check GPU's temperature

```python
# sudo python3 pyGPUtermlimit.py

from os import system
from time import sleep

while(True):

	system("nvidia-smi -q -d temperature > gputemp.txt")

	system("perl -ne 'print/([0-9]+)/ if /GPU Current Temp/i' gputemp.txt > currenttemp.txt")

	with open('currenttemp.txt', 'r') as fp:
	    temperature = fp.readlines()

	if int(temperature[0]) < 90:
		system("echo 'Temperature of GPU =' $(cat currenttemp.txt) '℃'") 
		print()
	else:
		system("sudo reboot")
	sleep(21)
```

## Sources

* [Ollama. Быстрый старт](https://the-president.ru/ollama-start)
* [llama3.2-vision](https://ollama.com/library/llama3.2-vision)
* [OCR: Document to Markdown](https://llamaocr.com/)
* [T5: Преобразователи текста в текст (часть первая)](https://questu.ru/articles/741909/)
* [Использование языковых моделей T5 для задачи упрощения текста](https://swsys.ru/index.php?page=article&id=4995&lang=ru)
* [Революция ChatGPT: освоение искусственного интеллекта с помощью специальных инструкций](https://questu.ru/articles/771672/)
* [Datasets:EdinburghNLP/xsum](https://huggingface.co/datasets/EdinburghNLP/xsum)
* [What is FLAN-T5? Is FLAN-T5 a better alternative to GPT-3?](https://exemplary.ai/blog/flan-t5)
* [Machine Translation with Transformer in Python](https://www.geeksforgeeks.org/machine-translation-with-transformer-in-python/)
* [Осваиваем T5 (text-to-text transfer transformer). Fine-Tuning](https://habr.com/ru/articles/762140/)
* [google/flan-t5-xl](https://huggingface.co/google/flan-t5-xl)
* [google/switch-base-8](https://huggingface.co/google/switch-base-8)
* [google/flan-t5-small](https://huggingface.co/google/flan-t5-small)
* [google-t5/t5-small](https://huggingface.co/google-t5/t5-small)
* [t5-small](https://www.aimodels.fyi/models/huggingFace/t5-small-google-t5)
* [Fine-Tuning the Pre-Trained T5-Small Model in Hugging Face for Text Summarization](https://medium.com/@anyuanay/fine-tuning-the-pre-trained-t5-small-model-in-hugging-face-for-text-summarization-3d48eb3c4360)
* [Fine Tuning Large Language Model (LLM)](https://www.geeksforgeeks.org/fine-tuning-large-language-model-llm/)
* [google/flan-t5-base](https://huggingface.co/google/flan-t5-base)
* [knkarthick/dialogsum](https://huggingface.co/datasets/knkarthick/dialogsum)
* [Введение в библиотеку Transformers и платформу Hugging Face](https://habr.com/ru/articles/704592/)
* [$ ollama run llama3.2 "Summarize this file: $(cat README.md)"](https://github.com/ollama/ollama#customize-your-own-model)
* [How to set ollama temperature from command line](https://genai.stackexchange.com/questions/699/how-to-set-ollama-temperature-from-command-line)
* https://askubuntu.com/questions/1249921/i-cant-see-my-internet-speed-on-conky
