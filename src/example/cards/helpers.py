# -*- encoding: utf-8 -*-
from .models import Card, CardStatus, CardOperateType, CardInfo, CardHistory

import datetime

def OpenAccount():
        cardstatus = CardStatus()
        cardstatus.name = input('状态:')
        cardstatus.remark = input('备注:')
        cardstatus.save()

        card = Card()
        card.balance=input('存款金额：')
        card.balance_available=card.balance
        card.balance_freeze=0
        card.status = cardstatus
        card.save()

        cardinfo = CardInfo()
        cardinfo.name=input('姓名：')
        cardinfo.phone=input('电话号码:')
        cardinfo.emil=input('邮箱：')
        cardinfo.card = card
        cardinfo.save()

        cardoperatetype=CardOperateType()
        cardoperatetype.name=input('请输入操作:')
        cardoperatetype.remark=input('备注:')
        cardoperatetype.save()

        card_history=CardHistory()
        card_history.time = datetime.datetime.now()
        # card_history.remark='''
        #     银行卡
        #     余额
        # '''.format(
        #     card,
        #     card.balance
        # )
        card_history.card=card
        card_history.operate=cardoperatetype
        card_history.save()

