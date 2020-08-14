# ansible-role-rsyslog [![Build Status](https://travis-ci.org/izumimatsuo/ansible-role-rsyslog.svg?branch=master)](https://travis-ci.org/izumimatsuo/ansible-role-rsyslog)

CentOS7 に rsyslog を導入する ansible role です。

## 設定項目

以下の設定項目は上書き可能。

| 項目名              | デフォルト値| 説明                 |
| ------------------- | ----------- | -------------------- |
| rsyslog_is_reciver  | no          | 受信用として構成する |
| rsyslog_recive_host | none        | 受信用ホスト         |
| rsyslog_listen_port | 514         | 受信用ポート番号     |
