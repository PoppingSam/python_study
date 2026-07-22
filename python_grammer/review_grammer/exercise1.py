'''
图书管理系统
'''
#%%
books = [
    {"书名": "三体", "author": "刘慈欣", "publisher": "重庆出版社"},
    {"书名": "活着", "author": "余华", "publisher": "作家出版社"},
    {"书名": "西游记", "author": "吴承恩", "publisher": "中华书局"},
]

choice = input(f"1. 借书\n 2. 还书\n 3. 查询\n 4. 退出\n")

if choice == "1":
    print("借书成功")

elif choice == "2":
    print("还书成功")

elif choice == "3":
    search = input(f"请输入书名或作者: ")
    for book in books:
        if book["书名"] == search or book["author"] == search:
            print("您要查询的书籍:")
            print(f"{'书名'.ljust(10)}{'作者'.ljust(10)}")
            print(f"{book['书名'].ljust(10)}{book['author'].ljust(10)}")
            break
    else:
        print(f"{search}未找到")

elif choice == "4":
    print("已退出")

