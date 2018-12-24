urls = {
    "GetMovieDayBoxOfficeList": {
        "info": "视频获取列表",
        "req_url": "/API/DataBox/Movie/GetMovieDayBoxOfficeList",
        "req_type": "post",
        "Referer": "https://app.endata.com.cn/DataBox/Film/Movie/Index",
        "Host": "app.endata.com.cn",
        "re_try": 1,
        "re_time": 0.1,
        "is_logger": True,
        "is_json": True,
    },
    "MovieDataByDetail": {
        "info": "视频详情",
        "req_url": "/API/DataBox/Movie/MovieDataByDetail",
        "req_type": "post",
        "Referer": "https://app.endata.com.cn/DataBox/Film/Movie/Index",
        "Host": "app.endata.com.cn",
        "re_try": 1,
        "re_time": 0.1,
        "is_logger": True,
        "is_json": True,
    },
    "MovieDataByBaseInfo": {
        "info": "视频大致信息， 获取EFMTMovieID来源",
        "req_url": "/API/DataBox/Movie/MovieDataByBaseInfo",
        "req_type": "post",
        "Referer": "https://app.endata.com.cn/DataBox/Film/Movie/Index",
        "Host": "app.endata.com.cn",
        "re_try": 1,
        "re_time": 0.1,
        "is_logger": True,
        "is_json": True,
    },
    "MovieDataByAudience": {
        "info": "营销指数",
        "req_url": "/API/DataBox/Movie/MovieDataByAudience",
        "req_type": "post",
        "Referer": "https://app.endata.com.cn/DataBox/Film/Movie/Index",
        "Host": "app.endata.com.cn",
        "re_try": 1,
        "re_time": 0.1,
        "is_logger": True,
        "is_json": True,
    },
    "new_search_subjects": {
        "info": "豆瓣电影",
        "req_url": "/j/new_search_subjects?sort=T&range=0,10&tags=电影&start={}",
        "req_type": "get",
        "Referer": "https://movie.douban.com",
        "Host": "movie.douban.com",
        "re_try": 1,
        "re_time": 0.1,
        "is_logger": True,
        "is_json": True,
    },
    "search": {
        "info": "搜索",
        "req_url": "/ajax/search?kw={}&cityId=30&stype=-1",
        "req_type": "get",
        "Referer": "http://m.maoyan.com",
        "Host": "m.maoyan.com",
        "re_try": 1,
        "re_time": 0.1,
        "is_logger": True,
        "is_json": True,
    },
    "comments": {
        "info": "获取评论，根据日期",
        "req_url": "/mmdb/comments/movie/{}.json?_v_=yes&offset={}&startTime={}",
        "req_type": "get",
        "Referer": "https://m.maoyan.com",
        "Host": "m.maoyan.com",
        "http": "http",
        "re_try": 1,
        "re_time": 0.1,
        "is_logger": True,
        "is_json": True,
    },
    "promption": {
        "info": "获取评论，根据日期",
        "req_url": "/movie/{}/promption-ajax?method=change&type={}&typeId=0&date={}__{}",
        "req_type": "get",
        "Referer": "https://pf.maoyan.com",
        "Host": "pf.maoyan.com",
        "http": "http",
        "re_try": 1,
        "re_time": 0.1,
        "is_logger": True,
        "is_json": True,
    },
    "getMarketIndex": {
        "info": "获取营销数据",
        "req_url": "/Movie/GetMarketIndex?mId={}",
        "req_type": "get",
        "Referer": "http://m.cbooo.cn",
        "Host": "m.cbooo.cn",
        "http": "http",
        "re_try": 1,
        "re_time": 0.1,
        "is_logger": True,
        "is_json": True,
    },
    "getDataBox": {
        "info": "根据地点获取电影信息",
        "req_url": "/API/DataBox/Movie/MovieDataBy{}",
        "req_type": "post",
        "Referer": "https://app.endata.com.cn",
        "Host": "app.endata.com.cn",
        "re_try": 1,
        "re_time": 0.1,
        "is_logger": True,
        "is_json": True,
    },
}