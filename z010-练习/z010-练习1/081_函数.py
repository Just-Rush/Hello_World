#练习8.3...
def make_shirt(size,textual):
    '''打印一个句子能够说明衣服的尺码和字样'''
    print(f'衣服的尺码是{size}英尺,上面印有的图案是{textual}')

make_shirt(size='5',textual='超牛')
make_shirt(size='10',textual='111')

def describe_city(name,country='中国'):
    '''打印一个城市所属的国家'''
    print(f'{name}位于{country}')

describe_city('香港')
describe_city('梵蒂冈','不知道哪里')
describe_city(name='玻利维亚',country='不知道哪里')

def make_album(singer_name,album_name,song_amounts=None):
    albums = {'singer':singer_name,'album':album_name,"amounts":song_amounts}
    #return albums
    print(albums)
make_album('a','b')

def make_album1(singer_name,album_name,song_amounts=None):
    albums = {'singer':singer_name,'album':album_name,"amounts":song_amounts}
    return albums
album = make_album1('a','b','3')
print(album)
"""上面两个：使用return返回和直接在函数里用print没有区别啊
使用return的优点应该在其他地方"""

'''在函数中加入循环并不像我想的那么简单
题目的意思也不是让在函数中使用循环完成'''
# def make_album2(singer_name=None,album_name=None,song_amounts=None):
#     albums2 = {'singer':singer_name,'album':album_name,"amounts":song_amounts}
#     while True:
#         print('请输入专辑信息，在任意时刻输入空格退出程序')
#         singer_name = input('请输入歌手名')
#         if singer_name == ' ':
#             break
#         album_name = input('请输入专辑名')
#         if album_name == ' ':
#             break
#         song_amounts = input('请输入歌曲数量')
#         print(albums2)
# a = make_album2()

#8.8
def make_album2(singer_name,album_name,song_amounts=None):
    albums2 = {'singer':singer_name,'album':album_name,"amounts":song_amounts}
    return albums2
while True:
    a = input('输入singer name:')
    if a == ' ':
        break
    b = input('输入album name:')
    if b == ' ':
        break
    c = input('输入歌曲数量：')
    if c == ' ':
        break
    print(make_album2(a,b,c))
print('感谢你的使用')
'''但是我不能在循环结束后打印一个包含总的输入的字典'''

