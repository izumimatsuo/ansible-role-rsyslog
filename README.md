# ansible-role-rsyslog [![Build Status](https://travis-ci.org/izumimatsuo/ansible-role-rsyslog.svg?branch=master)](https://travis-ci.org/izumimatsuo/ansible-role-rsyslog)

CentOS7 に rsyslog を導入する ansible role です。

- ```rsyslog_is_reciver``` と ```rsyslog_recive_host``` を設定することでリモート転送可能となる

## 設定項目

以下の設定項目は上書き可能。

| 項目名                      | デフォルト値| 説明                        |
| --------------------------- | ----------- | --------------------------- |
| rsyslog_reciver_listen_port | 514         | 受信用ポート番号            |
| rsyslog_reciver_hostnames   | none        | 受信用ホストの inventory 名 |
