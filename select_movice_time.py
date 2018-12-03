from config.RedisUtils import redisUtils

redisConn = redisUtils().redis_conn()

movies = """速度与激情7
变形金刚4：绝迹重生
复仇者联盟2：奥创纪元
变形金刚3
霍比特人：五军之战
星际穿越
美国队长2：冬日战士
X战警：逆转未来
猩球崛起：黎明之战
环太平洋
碟中谍4
末日崩塌
功夫熊猫2
银河护卫队
超凡蜘蛛侠2
少年派的奇幻漂流
复仇者联盟
超能陆战队
黑衣人3
哥斯拉
加勒比海盗4：惊涛怪浪
霍比特人：史矛革之战
冰川时代4：大陆漂移
灰姑娘
地心引力
速度与激情6
极品飞车
明日边缘
驯龙高手2
疯狂原始人
超人：钢铁之躯
忍者神龟：变种时代
地心历险记2：神秘岛
007：大破天幕杀机
终结者：创世纪
星际迷航：暗黑无界
雷神2：黑暗世界
蝙蝠侠：黑暗骑士崛起
特种部队：全面反击
敢死队2
博物馆奇妙夜3
霍比特人1：意外旅程
机械战警
超凡蜘蛛侠
冰雪奇缘
沉睡魔咒
木星上行
异星战场
蓝精灵
速度与激情5
金刚狼2
里约大冒险2
洛杉矶之战
饥饿游戏3：嘲笑鸟（上）
普罗米修斯
重返地球
谍影重重4
马达加斯加3
怪兽大学
虎胆龙威5
大侦探福尔摩斯2
猩球崛起
惊天危机
饥饿游戏
疯狂外星人
一触即发
诸神之怒
极乐空间
移动迷宫
遗落战境
安德的游戏
青蜂侠
蓝精灵2
致命伴旅
铁甲钢拳
环形使者
超验骇客
纳尼亚传奇3
天才眼镜狗
狂怒
战马
创战纪
明日世界
全面回忆
关键第四号
极速蜗牛
不惧风暴
分歧者2：绝地反击
超能查派
雷神
侠探杰克
了不起的盖茨比
宙斯之子：赫拉克勒斯
独行侠
惊天战神
美国队长
无敌破坏王
绿灯侠
巨人捕手杰克
森林战士
背水一战
盟军夺宝队
美少女特攻队
神奇海盗团
坚不可摧
雨果
被解救的姜戈
特工争风
老雷斯的故事
亡命地中海
安妮：纽约奇缘
敢死队3
神偷奶爸2
金蝉脱壳
云图
惊天魔盗团
生化危机5：惩罚
空中营救
庞贝末日
机械师
分歧者：异类觉醒
精灵旅社
源代码
天际浩劫
灵魂战车2：复仇时刻
别惹我
赤焰战场2
模仿游戏
致命黑兰
火鸡总动员
狂暴飞车
屠魔战士
王者之剑
劫案迷云
白雪公主之魔镜魔镜
奥林匹斯的陷落
三个火枪手
人狼大战
女巫季节
抢劫坚果店
驱魔者
太空一号
铁血精英
暮光之城4：破晓（上）
家园防线
蜂鸟特攻
赤焰战场
特警判官
圣杯神器：骸骨之城
非常小特工之时间大盗
大力神3D
破坏者
危情三日
整编特工
贵族大盗
美国骗局
再次出发
梦宅诡影
激战运钞车
赤警威龙
乔布斯
一夜迷情
迷踪：第九鹰团
夺命追踪
白昼冷光
不明身份
双雄
林肯律师
无处可逃
夺命深渊
赛车总动员2
丛林有情狼
碟中谍5：神秘国度
小黄人大眼萌
像素大战
头脑特工队
蚁人
小飞侠：幻梦启航
绝命海拔
移动迷宫2
史努比：花生大电影
007：幽灵党
饥饿游戏3：嘲笑鸟（下）
火星救援
海绵宝宝
精灵旅社2
极速风流
星球大战：原力觉醒
云中行走
鼠来宝4：萌在囧途
疯狂动物城
飞鹰艾迪
蝙蝠侠大战超人：正义黎明
伦敦陷落
奇幻森林
猎神：冬日之战
美国队长3：英雄内战
愤怒的小鸟
爱丽丝梦游仙境2：镜中奇遇记
X战警：天启
海底总动员2：多莉去哪儿
独立日：卷土重来
忍者神龟2：破影而出
泰山归来：险战丛林
爱宠大机密
谍影重重5
冰河时代5：星际碰撞
星际迷航3：超越星辰
鲨滩
逗鸟外传：萌宝满天飞
宾虚
侠探杰克：永不回头
但丁密码
奇异博士
邻家大贱谍
神奇动物在哪里
海洋奇缘
间谍同盟
佩小姐的奇幻城堡
最后的巫师猎人
末日迷踪
谍影特工
地心营救
神战：权力之眼
荒野猎人
灵偶契约
废柴特工
幻体：续命游戏
超脑48小时
分歧者3：忠诚世界
惊天魔盗团2
红色警戒999
铁拳
圆梦巨人
机械师2：复活
钢铁骑士
深海浩劫
萨利机长
速度与激情8
变形金刚5：最后的骑士
加勒比海盗5：死无对证
金刚：骷髅岛
生化危机：终章
极限特工：终极回归
寻梦环游记
神偷奶爸3
蜘蛛侠：英雄归来
雷神3：诸神黄昏
猩球崛起3：终极之战
金刚狼3：殊死一战
正义联盟
银河护卫队2
新木乃伊
神奇女侠
一条狗的使命
美女与野兽
星球大战外传：侠盗一号
王牌特工2：黄金圈
全球风暴
敦刻尔克
太空旅客
异形：契约
爱乐之城
东方快车谋杀案
欢乐好声音
攻壳机动队
蓝精灵：寻找神秘村
刺客信条
王牌保镖
赛车总动员3：极速挑战
异星觉醒
降临
极盗车神
银翼杀手2049
亚瑟王：斗兽争霸
魔弦传说
乐高蝙蝠侠大电影
鲨海
至暗时刻
超凡战队
恐袭波士顿
天才捕手
当怪物来敲门
玩命直播
回到火星
勇往直前
海边的曼彻斯特
迷失Z城
单身日记：好孕来袭
刺杀盖世太保
银河守卫队
双面劫匪
末日重启
空难余波
24小时：末路重生
爱在记忆消逝前
比得兔
超人总动员2
第一夫人
夺命来电
凤凰城遗忘录
复仇者联盟3：无限战争
公牛历险记
古墓丽影：源起之战
黑豹
环太平洋：雷霆再起
忌日快乐
寂静之地
金钱世界
绝命时钟2:22
狂暴巨兽
妈妈咪鸭
马戏之王
迷镇凶案
奇迹男孩
犬之岛
三块广告牌
深海越狱
水形物语
通勤营救
头号玩家
小马宝莉大电影
星球大战：最后的绝地武士
湮灭
移动迷宫3：死亡解药
勇敢者游戏：决战丛林
游侠索罗：星球大战外传
战犬瑞克斯
侏罗纪世界"""

video_name = movies.split("\n")
for _video_name in video_name:
    print(_video_name, redisConn.get("_video_name"))
