# Gas Fever ⛽🔥

Monitors Ethereum gas prices and sends Telegram alerts when the price exceeds your threshold.

## Features
- Real-time Ethereum gas tracking via Etherscan
- Telegram notifications for spikes in gas price
- Fully configurable via environment variables

## Usage

### 1. Set Environment Variables

```bash
export TELEGRAM_TOKEN=your_telegram_bot_token
export TELEGRAM_CHAT_ID=your_telegram_chat_id
export ALERT_THRESHOLD=90
