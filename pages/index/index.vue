<template>
	<view class="uni-list-container">

		<swiper class="uni-margin-swiper" circular :indicator-dots="indicatorDots" :autoplay="autoplay"
			:interval="interval" :duration="duration">
			<swiper-item>
				<view class="swiper-item uni-bg-red">A</view>
			</swiper-item>
			<swiper-item>
				<view class="swiper-item uni-bg-green">B</view>
			</swiper-item>
			<swiper-item>
				<view class="swiper-item uni-bg-blue">C</view>
			</swiper-item>
		</swiper>
		<view class="uni-text-icon" @click="goDetailPage(1)">
						22222
					</view>
		<scroll-view :scroll-top="scrollTop" scroll-with-animation scroll-y="true" class="scroll-Y" @scroll="scroll"
			ref="getheight">
			<view class="uni-padding-wrap uni-common-mt">
				<view class="uni-list-text" v-for="(num,index) in data" :key="index" @click="goDetailPage(index)">
					<view class="uni-text-icon">
						<image class="uni-text-img" src="../../static/c1.png" />
					</view>
					<text>待接待用户 - {{num}}</text>
				</view>
				<view class="uni-loadmore" v-if="showLoadMore">{{loadMoreText}}</view>
			</view>
		</scroll-view>
		<!-- <uni-link :href="href" :text="href"></uni-link> -->
	</view>
</template>

<script>
	export default {
		data() {
			return {
				href: 'https://uniapp.dcloud.io/component/README?id=uniui',
				indicatorDots: true,
				autoplay: true,
				interval: 2000,
				duration: 1000,
				scrollTop: 0,
				data: [],
				loadMoreText: "加载中...",
				showLoadMore: false,
				max: 0
			}
		},
		onLoad() {
			this.initData();
		},
		onUnload() {
			this.max = 0,
				this.data = [],
				this.loadMoreText = "加载更多",
				this.showLoadMore = false;
		},
		onReachBottom() {
			console.log("onReachBottom");
			if (this.max > 40) {
				this.loadMoreText = "没有更多数据了!"
				return;
			}
			this.showLoadMore = true;
			setTimeout(() => {
				this.setListData();
			}, 300);
		},
		onPullDownRefresh() {
			console.log('onPullDownRefresh');
			this.initData();
		},
		methods: {
			initData() {
				setTimeout(() => {
					this.max = 0;
					this.data = [];
					let data = [];
					this.max += 20;
					for (var i = this.max - 19; i < this.max + 1; i++) {
						data.push(i)
					}
					this.data = this.data.concat(data);
					uni.stopPullDownRefresh();
				}, 300);
			},
			setListData() {
				let data = [];
				this.max += 10;
				for (var i = this.max - 9; i < this.max + 1; i++) {
					data.push(i)
				}
				this.data = this.data.concat(data);
			},
			scroll(e) {
				console.log('scroll----', e)
				// this.scrollTop =  e.detail.scrollTop + 20
				this.scrollTop = e.detail.scrollTop
			},
			goDetailPage(num) {
				uni.switchTab({
					url: "/pages/tabBar/index"
				})
			},
		}
	}
</script>

<style lang="less" scoped>
	.uni-list-container {
		padding: 16rpx;
		display: flex;
		flex-direction: column;
		justify-content: flex-start;
		height: 100%;

		.uni-margin-swiper {
			position: relative;
			height: 300rpx;

			.swiper-item {
				height: 100%;
			}
		}

		.scroll-Y {
			height: calc(100vh - 400rpx);
			padding: 24rpx 0 24rpx 0;
      .uni-padding-wrap{
				padding: 0;
			}
			// flex: 1;
			.uni-list-text {
				margin: 16rpx 0;
				width: 100%;
				background-color: #fff;
				height: 120rpx;
				line-height: 12rpx;
				color: #555;
				border-radius: 4rpx;
				display: flex;
				flex-direction: row;
				align-items: center;
				justify-content: flex-start;
				padding: 0 16rpx 0 16rpx;

				.uni-text-icon {
					width: 80rpx;
					height: 80rpx;
					border-radius: 55%;
					overflow: hidden;
					border: 1rpx solid #cecaca;
					margin-right: 8rpx;
				}

				.uni-text-img {
					width: 100%;
					height: 100%;
				}
			}
		}


	}
</style>
