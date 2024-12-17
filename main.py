import pyautogui
import tkinter as tk

def ss_btn_click():
    """
    スクリーンショットを撮影し、半透明なウィンドウを生成し、表示する
    :return:
    """
# TODO クリックしたウィンドウのスクリーンショットを撮る？
    ss = pyautogui.screenshot()
    ss_pass = 'screenshot/ss.png'
    ss.save(ss_pass)
    print('スクリーンショットを保存しました。')

    window = tk.Tk()
    window.title('スクリーンショット透明化くん')

    # ウィンドウサイズの指定
    window.geometry("500x500")
    window.resizable(True, True)

    # ウィンドウの透明度
    window.attributes('-alpha', 0.7)

    # ウィンドウを前面で固定する
    # window.attributes('-topmost', True)

    img = tk.PhotoImage(file=ss_pass, master=window)
    label_img = tk.Label(window, image=img)
    label_img.pack()
    window.mainloop()

    # TODO 設定メニューの作成
    # TODO ショートカットキー
    # TODO 範囲指定をするか
    # TODO ウィンドウサイズ
    # TODO 透明度
    # TODO ウィンドウを閉じるときファイルを削除するか


if __name__ == '__main__':
    # マウスカーソルが画面の隅に移動するとスクリプト強制終了（安全機構）
    pyautogui.FAILSAFE = True  # デフォルトで有効

    # メインウィンドウ生成
    # TODO 最前面チェックあり
    root = tk.Tk()
    root.geometry("300x50")
    root.resizable(True, True)
    root.title('スクリーンショット透明化くん')
    # ウィンドウを前面で固定する
    root.attributes('-topmost', True)

    # 撮影ボタン
    btn_ss = tk.Button(root, width=10, height=5, text='開　始', command=ss_btn_click)
    btn_ss.pack()

    root.mainloop()
