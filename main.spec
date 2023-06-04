# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(
    [
        'main.py',
        'core\\data\\__init__.py',
        'core\\data\\parse.py',
        'core\\data\\request.py',
        'core\\static\\__init__.py',
        'core\\static\\define.py',
        'core\\support\\__init__.py',
        'core\\support\\coderunner.py',
        'core\\support\\decorator.py',
        'core\\support\\event_filter.py',
        'core\\support\\initialize.py',
        'core\\support\\json_minify.py',
        'core\\support\\msg_printer.py',
        'core\\support\\tools.py',
        'core\\sys\\__init__.py',
        'core\\sys\\accountstate.py',
        'core\\sys\\cloud.py',
        'core\\sys\\configuration.py',
        'core\\sys\\emails.py',
        'core\\sys\\file.py',
        'core\\sys\\globalv.py',
        'core\\sys\\log.py',
        'core\\sys\\path.py',
        'core\\sys\\settings.py',
        'core\\sys\\themes.py',
        'ui\\dialog\\__init__.py',
        'ui\\dialog\\ConfigOnlineSearcher.py',
        'ui\\dialog\\ConfigShareMsgInput.py',
        'ui\\dialog\\Dialog_ConfigMessageInput.py',
        'ui\\dialog\\Dialog_ScriptMessageInput.py',
        'ui\\dialog\\Dialog_ScriptTest.py',
        'ui\\dialog\\Dialog_Select.py',
        'ui\\dialog\\Input.py',
        'ui\\dialog\\Login.py',
        'ui\\dialog\\Message.py',
        'ui\\dialog\\Notice.py',
        'ui\\dialog\\Question.py',
        'ui\\func\\__init__.py',
        'ui\\func\\iconsetter.py',
        'ui\\pages\\__init__.py',
        'ui\\pages\\Ui_MainPagesContainer.py',
        'ui\\pages\\account\\__init__.py',
        'ui\\pages\\account\\AccountPage.py',
        'ui\\pages\\account\\Function.py',
        'ui\\pages\\account\\Ui_AccountPage.py',
        'ui\\pages\\cloud\\__init__.py',
        'ui\\pages\\cloud\\CloudPage.py',
        'ui\\pages\\cloud\\Function.py',
        'ui\\pages\\cloud\\Ui_CloudOverview.py',
        'ui\\pages\\cloud\\Ui_CloudPage.py',
        'ui\\pages\\cloud\\Ui_CloudRead.py',
        'ui\\pages\\config\\__init__.py',
        'ui\\pages\\config\\ConfigurationPage.py',
        'ui\\pages\\config\\Function.py',
        'ui\\pages\\config\\Ui_ConfigJsonEditor.py',
        'ui\\pages\\config\\Ui_ConfigurationEditor.py',
        'ui\\pages\\config\\Ui_ConfigurationOverview.py',
        'ui\\pages\\config\\Ui_ConfigurationPage.py',
        'ui\\pages\\script\\__init__.py',
        'ui\\pages\\script\\Function.py',
        'ui\\pages\\script\\ScriptPage.py',
        'ui\\pages\\script\\Ui_ScriptEditor.py',
        'ui\\pages\\script\\Ui_ScriptOverview.py',
        'ui\\pages\\script\\Ui_ScriptPage.py',
        'ui\\pages\\start\\__init__.py',
        'ui\\pages\\start\\Function.py',
        'ui\\pages\\start\\StartPage.py',
        'ui\\pages\\start\\Ui_ProgramRunner.py',
        'ui\\pages\\start\\Ui_StartPage.py',
        'ui\\pages\\start\\Ui_StartPageBtn.py',
        'ui\\pages\\tempview\\__init__.py',
        'ui\\pages\\tempview\\Function.py',
        'ui\\pages\\tempview\\TempviewPage.py',
        'ui\\pages\\tempview\\Ui_TemoviewRead.py',
        'ui\\pages\\tempview\\Ui_TempviewIndex.py',
        'ui\\pages\\tempview\\Ui_TempviewPage.py',
        'ui\\preload\\imp_qt.py',
        'ui\\widgets\\__init__.py',
        'ui\\widgets\\circular_progress\\__init__.py',
        'ui\\widgets\\circular_progress\\circular_progress.py',
        'ui\\widgets\\combo_box\\__init__.py',
        'ui\\widgets\\combo_box\\combo_box.py',
        'ui\\widgets\\credits_bar\\__init__.py',
        'ui\\widgets\\credits_bar\\credits.py',
        'ui\\widgets\\grips\\__init__.py',
        'ui\\widgets\\grips\\grips.py',
        'ui\\widgets\\grips\\widgets.py',
        'ui\\widgets\\group_box\\__init__.py',
        'ui\\widgets\\group_box\\group_box.py',
        'ui\\widgets\\icon_button\\__init__.py',
        'ui\\widgets\\icon_button\\icon_button.py',
        'ui\\widgets\\line_edit\\__init__.py',
        'ui\\widgets\\line_edit\\line_edit.py',
        'ui\\widgets\\list\\__init__.py',
        'ui\\widgets\\list\\list.py',
        'ui\\widgets\\navigation\\__init__.py',
        'ui\\widgets\\navigation\\nav_button.py',
        'ui\\widgets\\navigation\\navigation.py',
        'ui\\widgets\\navigation\\sep_line.py',
        'ui\\widgets\\navigation\\tooltip.py',
        'ui\\widgets\\navigation\\ui_navigation.py',
        'ui\\widgets\\push_button\\__init__.py',
        'ui\\widgets\\push_button\\push_button.py',
        'ui\\widgets\\scroll_area\\__init__.py',
        'ui\\widgets\\scroll_area\\scroll_area.py',
        'ui\\widgets\\slider\\__init__.py',
        'ui\\widgets\\slider\\slider.py',
        'ui\\widgets\\spin_box\\__init__.py',
        'ui\\widgets\\spin_box\\spin_box.py',
        'ui\\widgets\\table_widget\\__init__.py',
        'ui\\widgets\\table_widget\\table_widget.py',
        'ui\\widgets\\text_edit\\__init__.py',
        'ui\\widgets\\text_edit\\text_edit.py',
        'ui\\widgets\\title_bar\\__init__.py',
        'ui\\widgets\\title_bar\\sep_line.py',
        'ui\\widgets\\title_bar\\title_bar.py',
        'ui\\widgets\\title_bar\\title_button.py',
        'ui\\widgets\\title_bar\\tooltip.py',
        'ui\\widgets\\title_bar\\ui_title_bar.py',
        'ui\\widgets\\toggle\\__init__.py',
        'ui\\widgets\\toggle\\toggle.py',
        'ui\\widgets\\window\\__init__.py',
        'ui\\widgets\\window\\window.py',
        'ui\\windows\\main\\__init__.py',
        'ui\\windows\\main\\Function.py',
        'ui\\windows\\main\\MainWindow.py',
        'ui\\windows\\main\\Ui_MainWindow.py',
    ],
    pathex=["D:\\Workspace\\GitRepository\\General_Crawler_Tool"],
    binaries=[],
    datas=[],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='GeneralCrawlerTool_V0.6.2_DEV',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon='D:\\Workspace\\GitRepository\\General_Crawler_Tool\\icon.ico',
)
coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='main',
)
