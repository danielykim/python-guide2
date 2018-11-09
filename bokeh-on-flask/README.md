## Plotting Iris Data by Bokeh on Flask
Anaconda Prompt에서 아래 명령을 실행한 후
```bash
python bokeh_app.py
```

http://localhost:5000/ 에 접속해서 확인하면 됩니다.


## `bokeh_app.py` 설명
1. Backend에서 [pandas](https://pandas.pydata.org/)로 데이터를 가져옵니다.
2. [bokeh](https://bokeh.pydata.org)로 Interactive Plot을 그립니다.
3. Interactive Plot을 templates/iris.html 로 넘깁니다.


## 참고 자료
- https://palletsprojects.com/p/flask/
- http://flask.pocoo.org/docs/1.0/quickstart/#rendering-templates
- https://gist.github.com/ianschenck/977379a91154fe264897
- https://bokeh.pydata.org/en/latest/docs/gallery/iris.html
- https://bokeh.pydata.org/en/latest/docs/user_guide/embed.html#components
