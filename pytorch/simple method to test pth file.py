# This test file proved that the *.pth file we saved during training is only weights!
import torch
pthfile = r'D:\PycharmProjects2\inpainting_gmcnn\pytorch\checkpoints\20191012-135109_GMCNN_Thanka_b4_s256x256_gc32_dc64_randmask-rect_pretrain\10_net_GM.pth'
net_state_dict=torch.load(pthfile)
dict_name = list(net_state_dict)
for i, p in enumerate(dict_name):
    print(i, p)