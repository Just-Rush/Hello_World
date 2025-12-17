# 某些代码片段的记录
1. 
    ```python
    if all(k in data for k in ['e1', 'e2','e3', 'e7', 'e8', 'e9']):
    ```

    ![alt text](image.png)
2. 
    ```python
    with open(filepath, 'r') as f:
        for line in f:

    with open (out_file, 'r') as f:
        lines = f.readlines()
    for line in lines:
        
    with open (out_file, 'r') as f:
        lines = f.readlines()
        for line in lines:
    三种写法的差异
    ```
    ![alt text](image-1.png)

# pandas:
1. `.pivot()`,数据透视。重新设置数据的行列。https://blog.csdn.net/superY_26/article/details/112689493  