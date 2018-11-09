## Plotting iris data by matplotlib & seaborn on Flask
Anaconda Prompt에서 아래 명령을 실행한 후
```bash
python app.py
```

브라우저에서 http://localhost:5000/ 에 접속해서 확인하면 됩니다.


## `app.py` 설명
1. Backend에서 `pandas`로 데이터를 가져옵니다.
2. `matplotlib`와 `seaborn`을 이용하여 그림을 그립니다.
3. 그림을 base64로 Encoding 합니다.
4. Encoding한 그림을 templates/temp.html 로 넘겨줍니다.



## 참고 자료
- https://palletsprojects.com/p/flask/
- http://flask.pocoo.org/docs/1.0/quickstart/#rendering-templates
- https://gist.github.com/ianschenck/977379a91154fe264897
