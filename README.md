# ブレーカー落ち警報器（M5StickC用「WiSUN HAT」キット利用)

ブレーカーが落ちる直前にブザーで警報します

## Description
PHVの充電の際に家のブレーカーが落ちる問題に悩んでいたのですが、WiSUN通信でSmartMeterから現在の使用電力を入手できることを知り
警報デバイスを作成しました。(rukihena様の[参考ページ](https://qiita.com/rukihena/items/82266ed3a43e4b652adb))  
rin-ofumi様作の[WiSUN HATキット](https://github.com/rin-ofumi/m5stickc_wisun_hat)を利用しています。

## Requirement
以下のデバイスが必要です。
*[M5StickC](https://www.switch-science.com/catalog/5517/)　×2台
*[WiSUN HATキット](https://kitto-yakudatsu.booth.pm/items/1650727)
*[BP35A1](https://www.zaikostore.com/zaikostore/stockDetail?stockID=st29863403&productName_forFind=BP35A1&typeStock_forFind=all&productIdOfHitotsukara=pr6714723)
*[Speaker Hat](https://www.switch-science.com/catalog/5754/)

また、事前に[Bルートサービス](http://www.tepco.co.jp/pg/consignment/liberalization/smartmeter-broute.html)の申し込みが必要です。

1台のM5StickCは親機としてBP35A1とWiSUN HATキットを接続してスマートメーターに接続します。こちらのソフトの準備はrin-ofumi様作の[WiSUN HATキット](https://github.com/rin-ofumi/m5stickc_wisun_hat)を参照ください。

## Install
UI FlowでSmartMeter_RCV.m5fを読み込んで実行してください。

## Usage
電力使用量が高くなるにつれ、文字表示が青(マイナス)⇒白⇒赤⇒警報音と変わるようになっています。閾値は各家庭の契約電力に合わせて変えてください。

## Licence

[MIT](https://github.com/tcnksm/tool/blob/master/LICENCE)

## Author

[ういろう](https://github.com/willowslope)