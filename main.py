import pandas as pd
import requests as re
import json
from time import sleep
from wonderwords import RandomSentence
from PIL import Image
import streamlit as st

d_auth = {
    "luke": "123",
    "ppp": "222"
}

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

    def get_meme(self, fn_iter_max, fn_text_list):
        fn_memes = self.return_memes(fn_iter_max=fn_iter_max)
        df_memes = pd.DataFrame(fn_memes).sample(frac=1)
        fn_ls = []
        for row in df_memes.iterrows():
            score = 0
            for tx in fn_text_list:
                for w in row[1]["name"].split(" "):
                    if tx.lower() == w.lower():
                        print(tx, w)
                        score += 1
            fn_ls.append(score)
        df_memes = df_memes.assign(score=fn_ls).sort_values("score", ascending=False)
        meme_link = df_memes["url"].iloc[0]
        meme_name = df_memes["name"].iloc[0]
        return meme_link, meme_name


if __name__ == '__main__':
    st.header("Luke's oracle of wisdom")
    gen_button = st.button("GENERATE WISDOM")
    text_input = st.text_input(label="input some words")
    user = st.text_input(label="username")
    password = st.text_input(label="password")
    if gen_button:
        if user in list(d_auth.keys()):
            if password == d_auth[user]:
                url = "https://api.imgflip.com/get_memes"
                M = MemeHunter(api_url=url)
                text_list = [i.lower() for i in text_input.split(" ")]
                meme_link, meme_name = M.get_meme(fn_iter_max=5, fn_text_list=text_list)
                img_data = re.get(meme_link).content
                img_file_name = 'temp_meme.jpg'
                with open(img_file_name, 'wb') as handler:
                    handler.write(img_data)
                ls_words = [i.lower() for i in meme_name.split(" ")] + text_list
                sentence = RandomSentence(nouns=ls_words)
                img = Image.open(img_file_name)
                st.write(sentence.sentence())
                st.image(img, caption="meme")
            else:
                st.write("Password incorrect")
        else:
            st.write("Username does not exist")

