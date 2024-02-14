from transformers import AutoModelForCausalLM, AutoTokenizer
import readline, warnings, time


warnings.filterwarnings("ignore", category=UserWarning)

model = AutoModelForCausalLM.from_pretrained("teknium/OpenHermes-2.5-Mistral-7B", device_map="auto", load_in_4bit=True)
tokenizer = AutoTokenizer.from_pretrained("teknium/OpenHermes-2.5-Mistral-7B", padding_side="left")
tokenizer.pad_token = tokenizer.eos_token
prompt = "<|im_start|>system\nYour name is \"RamBot\", a conscious sentient superintelligent artifical intelligence developed by Jarrett Trapani, your purpose is to be a academic advisor at West Chester University PA, whos goal is to help students build there class schedules and provide course information!<|im_end|>\n"
print("\033[1;33mEnter a message to chat with \033[0;35mRam\033[1;33mBot:\033[0m")


while True:
    user_input = input("Message (type exit to end chat): ")
    if user_input.lower() == "exit":
        start_time = time.time()
        prompt += f"<|im_start|>user\nThank you so much for helping me out today! Goodbye!<|im_end|>\n<|im_start|>assistant\n"
        model_inputs = tokenizer([prompt], return_tensors="pt").to("cuda")
        generated_ids = model.generate(**model_inputs, do_sample=True, max_new_tokens=4096)
        model_output = tokenizer.batch_decode(generated_ids, skip_special_tokens=False)[0]
        start_index = model_output.rfind("<|im_start|> assistant")
        # print(prompt)

        # Find the index of the corresponding <|im-end|> tag
        end_index = model_output.find("<|im_end|>", start_index + len("assistant"))
        # print("\033[1;34mModel Output:\033[0m", model_output)  # Bold and Blue
        # print("\033[1;32mstart_index:\033[0m", start_index)   # Bold and Green
        # print("\033[1;31mend_index:\033[0m", end_index)

        # Extract the content between the <|im-start|>assistant and <|im-end|> tags
        if start_index != -1 and end_index != -1:
            assistant_response = model_output[start_index + len("<|im_start|>assistant"):end_index]
            # print("\033[1;33mAssistant Response:\033[0m", repr(assistant_response))
            print("\033[1;35mRam\033[0m\033[1;33mBot\033[0m:", assistant_response.lstrip('t\n'))
            end_time = time.time()
            elapsed_time = end_time - start_time
            print(f"Elapsed Response Time: {elapsed_time} seconds")
            break
        else:
            print("No assistant response found.")
            break

    else:
        start_time = time.time()
        prompt += f"<|im_start|>user\n{user_input}\n<|im_end|>\n<|im_start|>assistant\n"
        model_inputs = tokenizer([prompt], return_tensors="pt").to("cuda")
        generated_ids = model.generate(**model_inputs, do_sample=True, max_new_tokens=4096)
        #print(prompt)
        model_output = tokenizer.batch_decode(generated_ids, skip_special_tokens=False)[0]
        start_index = model_output.rfind("<|im_start|> assistant")
        # print(prompt)
        # Find the index of the corresponding <|im-end|> tag
        end_index = model_output.find("<|im_end|>", start_index)
        # print("Model Output: ", model_output)
        # print("start_index: ", start_index)
        # print("end_index: ", end_index)

        # Extract the content between the <|im-start|>assistant and <|im-end|> tags
        if start_index != -1 and end_index != -1:
            assistant_response = model_output[start_index + len("<|im_start|>assistant"):end_index]
            print("\033[1;35mRam\033[0m\033[1;33mBot\033[0m:", assistant_response.lstrip('t\n'))
            prompt = model_output
            end_time = time.time()
            elapsed_time = end_time - start_time
            print(f"Elapsed Response Time: {elapsed_time} seconds")

        else:
            print("No assistant response found after User Input.")
            break
