import modi

# 모디 연결
bundle = modi.MODI()

# ir센서 3개 사용(하나는 스캔, 두개는 엔코더용)
ir_encoder_1 = bundle.irs[0]
ir_encoder_2 = bundle.irs[1]
ir_encoder_head = bundle.irs[2]



# 센서 무한측정 test
while 1:
    print(ir_encoder_1, ir_encoder_2, ir_encoder_head, ir_encoder_1.proximity, ir_encoder_2.proximity, ir_encoder_head.proximity)
