import feffery_antd_components as fac
from dash.dependencies import Component


def render() -> Component:
    """渲染当前演示用例"""

    # 构造演示用例相关内容
    demo_contents = fac.AntdCascader(
        placeholder='请选择',
        options=[
            {
                'value': '节点1',
                'key': '节点1',
                'label': '节点1',
                'children': [
                    {'value': '节点1-1', 'key': '节点1-1', 'label': '节点1-1'},
                    {
                        'value': '节点1-2',
                        'label': '节点1-2',
                        'children': [
                            {'value': '节点1-2-1', 'label': '节点1-2-1'},
                            {'value': '节点1-2-2', 'label': '节点1-2-2'},
                        ],
                    },
                ],
            },
            {
                'value': '节点2',
                'label': '节点2',
                'children': [
                    {'value': '节点2-1', 'label': '节点2-1'},
                    {'value': '节点2-2', 'label': '节点2-2'},
                ],
            },
        ],
        optionsNodeKeyToLabel={
            '节点1': fac.AntdText('节点1', italic=True),
            '节点1-1': fac.AntdText(
                '节点1-1', strong=True, style={'color': 'red'}
            ),
        },
    )

    return demo_contents


code_string = [
    {
        'code': """
fac.AntdCascader(
    placeholder='请选择',
    options=[
        {
            'value': '节点1',
            'key': '节点1',
            'label': '节点1',
            'children': [
                {
                    'value': '节点1-1',
                    'key': '节点1-1',
                    'label': '节点1-1'
                },
                {
                    'value': '节点1-2',
                    'label': '节点1-2',
                    'children': [
                        {
                            'value': '节点1-2-1',
                            'label': '节点1-2-1'
                        },
                        {
                            'value': '节点1-2-2',
                            'label': '节点1-2-2'
                        }
                    ]
                }
            ]
        },
        {
            'value': '节点2',
            'label': '节点2',
            'children': [
                {
                    'value': '节点2-1',
                    'label': '节点2-1'
                },
                {
                    'value': '节点2-2',
                    'label': '节点2-2'
                }
            ]
        }
    ],
    optionsNodeKeyToLabel={
        '节点1': fac.AntdText('节点1', italic=True),
        '节点1-1': fac.AntdText(
            '节点1-1',
            strong=True,
            style={
                'color': 'red'
            }
        )
    }
)
"""
    }
]
