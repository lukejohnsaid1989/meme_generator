import requests as re
import json
from time import sleep
from random import randint
from wonderwords import RandomSentence
from PIL import Image
import streamlit as st


class MemeHunter:

    def __init__(self, api_url):
        self.api_url = api_url

    def return_memes(self, fn_iter_max):
        fn_resp = re.get(self.api_url)
        fn_flag = False
        fn_iter = 0
        while not fn_flag:
            if fn_resp.status_code == 200:
                fn_flag_meme_content = json.loads(fn_resp.content)
                if "data" in list(fn_flag_meme_content.keys()):
                    if "memes" in list(fn_flag_meme_content["data"].keys()):
                        return fn_flag_meme_content["data"]["memes"]
                    else:
                        raise Exception("meme key not found")
                else:
                    raise Exception("data key not found")
            else:
                sleep(1)
                fn_iter += 1
            if fn_iter == fn_iter_max:
                raise Exception("Connection timeout exceeded")

    def get_random_meme(self, fn_iter_max):
        fn_memes = self.return_memes(fn_iter_max=fn_iter_max)
        fn_meme = fn_memes[randint(0, len(fn_memes) - 1)]
        return fn_meme


if __name__ == '__main__':
    st.header("Luke's cool meme generator")
    gen_button = st.button("GENERATE MEME")
    if gen_button:
        url = "https://api.imgflip.com/get_memes"
        M = MemeHunter(api_url=url)
        meme = M.get_random_meme(fn_iter_max=5)
        img_data = re.get(meme["url"]).content
        img_file_name = 'temp_meme.jpg'
        with open(img_file_name, 'wb') as handler:
            handler.write(img_data)
        sentence = RandomSentence(nouns=[i.lower() for i in meme["name"].split(" ")])
        img = Image.open(img_file_name)
        st.write(sentence.sentence())
        st.image(img, caption="meme")
