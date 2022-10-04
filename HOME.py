import streamlit as st
from streamlit.logger import get_logger
from streamlit.components.v1 import html

LOGGER = get_logger(__name__)

st.set_page_config(
    page_title="ホーム | OptimAz",
    page_icon="📗"
)

st.caption("数理最適化 Webアプリ")
st.title("OptimAz")

st.info("👈 サイドバーから事例をを選んで Let's 数理最適化！")

with st.expander("🏫 クラス編成", expanded=True):
  single_col1, single_col2 = st.columns([2, 1])
  with single_col1:
    st.caption("こんなことを考える公立中学校教員のアナタに！")
    st.markdown("""
        * 最適なクラス編成をしたい
        * 自動化して教員の作業コストを削減したい
        * 柔軟にクラス編成のルールを変更したい
        * 感情に左右されずクラス編成をしたい
    """)
  with single_col2:
    st.image("images/shingakki_classgae.png")

st.markdown("---")

# SNSシェアボタン
html("""<a href="https://twitter.com/share?ref_src=twsrc%5Etfw" class="twitter-share-button" data-size="large" data-hashtags="OptimAz" data-url="https://github.com/Kitsuya0828/" data-text="数理最適化Webアプリ\n" data-lang="ja" data-show-count="false">Tweet</a><script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>
<div class="fb-share-button" data-href="https://github.com/Kitsuya0828/" data-layout="button" data-size="large"><a target="_blank" href="https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fgithub.com%2FKitsuya0828%2F&amp;src=sdkpreparse" class="fb-xfbml-parse-ignore">シェアする</a></div><div id="fb-root"></div><script async defer crossorigin="anonymous" src="https://connect.facebook.net/ja_JP/sdk.js#xfbml=1&version=v14.0" nonce="yGPVy76g"></script>
<style type="text/css">.fb_iframe_widget > span {vertical-align: baseline !important;}</style>""")