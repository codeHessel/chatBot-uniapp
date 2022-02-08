<template>
	<view class="uni-chat-container">
		<view class="uni-chat-title">
			<text class="uni-panel-text">聊天机器人</text>
		</view>
		<view class="uni-chat-content">
			<view class="uni-text-area-body">
				<scroll-view :scroll-top="scrollTop" scroll-with-animation scroll-y="true" class="scroll-Y"
					@scroll="scroll" ref="getheight">
					<view class="uni-text-area-list" v-for="(item,k) in txtList" :class="{'left':item.type == 0}">
						<view class="uni-text-icon left">
							<image class="uni-text-img" src="../../static/c1.png" />
						</view>
						<view class="uni-text-content">
							{{item.text}}
						</view>
						<view class="uni-text-icon right">
							<image class="uni-text-img" src="../../static/c1.png" />
						</view>
					</view>
				</scroll-view>
				<view class="uni-text-area-wrapper">
					<textarea border border-color="#777" class="wrapper-textarea" v-model="value"
						placeholder="请输入聊天内容……" />
					<view class="uni-text-area-btn">
						<button class="txt-btn" size="mini" type="primary" @click="submitTxt">发送</button>
					</view>
				</view>
			</view>
		</view>
	</view>
</template>

<script>
	export default {
		data() {
			return {
				value: '',
				txtList: [{
					text: '说点什么吧~',
					type: 0
				}],
				scrollTop: 0,
				oldscrollTop: 0,
			}
		},
		onUnload() {
			this.value = ""
		},
		methods: {
			submitTxt() {
				if (!this.value) {
					uni.showToast({
						icon: "none",
						title: "发送内容不能为空~"
					})
					return
				}
				const tmp = this.value
				this.value = ''
				console.log('---', this);
				this.txtList.push({
					text: tmp,
					type: 1
				})
				var that = this
				uni.request({
					url: "/api",
					method: 'POST',
					data: {
						"keyword": tmp
					},
					success(res) {
						that.value = ''
						console.log('获取suc：---', that, );
						that.txtList.push({
							text: res.data,
							type: 0
						})
						that.txtList.length && that.goBottom()
					},
					fail(err) {
						console.log('获取失败：', err, this);
					}
				})
			},
			goBottom() {
				const getHeight = this.$refs.getheight
				let height = getHeight.$el?.offsetHeight
				const children = getHeight.$children
				let sum = 0
				children?.forEach(item => {
					sum = sum + item?.$el?.offsetHeight || 0
				})
				if (sum > height - 45) {
					this.$nextTick(() => {
						this.scrollTop = sum + 90
						this.oldscrollTop = sum + 90
					});
				}
			},
			scroll(e) {
				console.log('scroll----', e)
				// this.scrollTop =  e.detail.scrollTop + 20
				this.oldscrollTop = e.detail.scrollTop
			}
		}
	}
</script>


<style lang="less">
	.uni-chat-container {
		padding: 16rpx 16rpx 0rpx 16rpx;
		display: flex;
		flex-direction: column;
		height: 100%;

		.scroll-Y {
			height: calc(100vh - 680rpx);
			//  height: 55vh;
			padding: 0;
			margin: 0;
		}

		.uni-chat-title {
			height: 28px;
			align-items: center;
			text-align: center;
			height: 28px;
			align-items: center;
			background: #e7e7e7;
			display: flex;
			align-items: center;
			justify-content: center;
		}

		.uni-chat-content {
			flex: 1;
			padding-bottom: 16rpx;
			display: flex;
			flex-direction: column;
		}

		.uni-text-area-body {
			flex: 1;
		}
	}

	.uni-text-area-list {
		display: flex;
		flex-direction: row;
		align-items: flex-start;
		justify-content: flex-end;
		margin-bottom: 16rpx;
		&:first-child{
			margin-top: 8rpx;
		}

		.uni-text-content {
			background: #7cb18485;
			border-radius: 5rpx;
			padding: 8rpx;
			margin-top: 12rpx;
			white-space: initial;
			word-break: break-all;
		}

		.uni-text-icon.right {
			display: block;
			margin-left: 8rpx;
		}

		.uni-text-icon.left {
			display: none;
		}

		.uni-text-content {
			max-width: calc(100% - 110rpx)
		}

		&.left {
			justify-content: flex-start;

			.uni-text-content {
				background: #ccc9c950;
			}

			.uni-text-icon.left {
				display: block;
				margin-right: 4rpx;
			}

			.uni-text-icon.right {
				display: none;
			}
		}
	}

	.uni-text-icon {
		width: 80rpx;
		height: 80rpx;
		border-radius: 55%;
		overflow: hidden;
		border: 1rpx solid #cecaca;
	}

	.uni-text-area-wrapper {
		padding-top: 30rpx;
		display: flex;
		flex-direction: column;
		height: 400rpx;

		.wrapper-textarea {
			flex: 1;
			background: #fff;
			padding: 8rpx;
			border-radius: 8rpx;
			width: auto;
		}
	}

	.uni-text-area-btn {
		margin-top: 32rpx;
		display: flex;
		flex-direction: row;
		justify-content: flex-end;

		.txt-btn {
			margin-right: 0;
		}
	}

	.uni-text-img {
		width: 100%;
		height: 100%;
	}
</style>
