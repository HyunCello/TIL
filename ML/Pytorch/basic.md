## nn.Conv2d

```python
nn.Conv2d(
		in_channels,
		out_channels,
		kernel_size,
		stride=1,
		padding=0,
		dilation=1,
		groups=1,
		bias=True,
		padding_mode='zeros'
)
```

- 파라미터 : `in_channels` , `out_channels` , `kernel_size`
- 나머지 파라미터는 기본값이 입력되어있음 + 일반적으로 많이 사용되는 값들
- input 값에 2d convolution 연산을 적용하는 함수 → 2d convolution은 뭘 하는데?
- input size = (<!-- $N,C_{in},H,W$ --> <img style="transform: translateY(0.1em); background: white;" src="https://render.githubusercontent.com/render/math?math=N%2CC_%7Bin%7D%2CH%2CW">), output = (<!-- $N,C_{out},H_{out},W_{out}$ --> <img style="transform: translateY(0.1em); background: white;" src="https://render.githubusercontent.com/render/math?math=N%2CC_%7Bout%7D%2CH_%7Bout%7D%2CW_%7Bout%7D">)
- $N$ = batch size, $C$ = 채널의 수