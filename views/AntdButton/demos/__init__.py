import feffery_antd_components as fac
from dash.dependencies import Component

from . import (
    basic_usage,  # noqa: F401
    button_types,  # noqa: F401
    sizes,  # noqa: F401
    disabled_status,  # noqa: F401
    danger_status,  # noqa: F401
    ghost_background,  # noqa: F401
    button_shape,  # noqa: F401
    block_button,  # noqa: F401
    as_link,  # noqa: F401
    button_icon,  # noqa: F401
    auto_insert_space,  # noqa: F401
    button_loading,  # noqa: F401
    auto_spin,  # noqa: F401
    motion_type,  # noqa: F401
    click_execute_js,  # noqa: F401
    basic_callbacks,  # noqa: F401
    auto_spin_callback,  # noqa: F401
)
from components import demos_render

demos_config = [
    {
        'path': 'basic_usage',
        'title': '基础使用',
        'description': fac.AntdParagraph('最基础的按钮。'),
    },
    {
        'path': 'button_types',
        'title': '按钮类型',
        'description': fac.AntdParagraph('不同类型的按钮。'),
    },
    {
        'path': 'sizes',
        'title': '尺寸规格',
        'description': fac.AntdParagraph('不同尺寸的按钮。'),
    },
    {
        'path': 'disabled_status',
        'title': '禁用状态',
        'description': fac.AntdParagraph(
            [
                '设置参数',
                fac.AntdText('disabled=True', code=True),
                '开启禁用状态。',
            ]
        ),
    },
    {
        'path': 'danger_status',
        'title': '危险状态',
        'description': fac.AntdParagraph(
            [
                '设置参数',
                fac.AntdText('danger=True', code=True),
                '开启危险状态。',
            ]
        ),
    },
    {
        'path': 'ghost_background',
        'title': '透明背景',
        'description': fac.AntdParagraph(
            [
                '设置参数',
                fac.AntdText('ghost=True', code=True),
                '开启透明背景。',
            ]
        ),
    },
    {
        'path': 'button_shape',
        'title': '按钮形状',
        'description': fac.AntdParagraph(
            [
                '设置参数',
                fac.AntdText('shape', code=True),
                '控制按钮形状。',
            ]
        ),
    },
    {
        'path': 'block_button',
        'title': '撑满父元素',
        'description': fac.AntdParagraph(
            [
                '设置参数',
                fac.AntdText('block=True', code=True),
                '撑满父元素。',
            ]
        ),
    },
    {
        'path': 'as_link',
        'title': '链接跳转功能',
        'description': fac.AntdParagraph(
            [
                '设置参数',
                fac.AntdText('href', code=True),
                '添加链接跳转功能。',
            ]
        ),
    },
    {
        'path': 'button_icon',
        'title': '额外图标',
        'description': fac.AntdParagraph(
            [
                '设置参数',
                fac.AntdText('icon', code=True),
                '添加自定义图标元素。',
            ]
        ),
    },
    {
        'path': 'auto_insert_space',
        'title': '汉字自动插入空格',
        'description': fac.AntdParagraph(
            [
                '设置参数',
                fac.AntdText('autoInsertSpace', code=True),
                '控制是否在按钮内容为两个汉字时，自动插入空格。',
            ]
        ),
    },
    {
        'path': 'button_loading',
        'title': '加载中状态',
        'description': fac.AntdParagraph(
            [
                '设置参数',
                fac.AntdText('loading', code=True),
                '控制是否将按钮渲染为加载中状态。',
            ]
        ),
    },
    {
        'path': 'auto_spin',
        'title': '点击自动进入加载中状态',
        'description': fac.AntdParagraph(
            [
                '设置参数',
                fac.AntdText('autoSpin', code=True),
                '控制按钮是否在每次被点击后自动进入加载中状态。',
            ]
        ),
    },
    {
        'path': 'motion_type',
        'title': '特殊交互动效',
        'description': fac.AntdParagraph(
            [
                '设置参数',
                fac.AntdText('motionType="happy-work"', code=True),
                '为按钮点击交互行为开启特殊交互动效。',
            ]
        ),
    },
    {
        'path': 'click_execute_js',
        'title': '点击直接执行js',
        'description': fac.AntdParagraph(
            [
                '通过参数',
                fac.AntdText('clickExecuteJsString', code=True),
                '为按钮设置每次点击后直接触发的',
                fac.AntdText('javascript', strong=True),
                '代码，从而在简单场景下省略编写回调函数。',
            ]
        ),
    },
    {
        'path': 'basic_callbacks',
        'title': '回调监听',
        'description': fac.AntdParagraph(
            [
                '通过',
                fac.AntdText('nClicks', code=True),
                '进行按钮点击事件的监听，特别地，在有效设置参数',
                fac.AntdText('debounceWait', code=True),
                '后，将针对点击事件进行防抖监听，避免过于频繁的触发。',
            ]
        ),
    },
    {
        'path': 'auto_spin_callback',
        'title': '配合autoSpin的回调',
        'description': fac.AntdParagraph(
            [
                '配合',
                fac.AntdText('autoSpin', code=True),
                '、',
                fac.AntdText('loadingChildren', code=True),
                '等参数优化点击按钮触发耗时计算任务执行的场景。',
            ]
        ),
    },
]


def render(component: Component, section_name: str = None) -> Component:
    """渲染当前组件演示用例"""

    return demos_render.render(
        component=component,
        demos_config=demos_config,
        section_name=section_name,
    )
