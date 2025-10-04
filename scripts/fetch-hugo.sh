#!/usr/bin/env bash
set -euo pipefail
VERSION=${1:-v0.151.0}

OS=$(uname -s | tr '[:upper:]' '[:lower:]')
ARCH=$(uname -m)
case $OS in
	darwin) PLATFORM="darwin-universal" ;;
	linux)
		if [[ $ARCH == "aarch64" || $ARCH == "arm64" ]]; then PLATFORM="linux-arm64"; else PLATFORM="linux-amd64"; fi ;;
	*) echo "Unsupported OS: $OS" >&2; exit 1 ;;
esac

ASSET="hugo_extended_${VERSION#v}_${PLATFORM}.tar.gz"
BASE_URL="https://github.com/gohugoio/hugo/releases/download/${VERSION}/${ASSET}"
MIRRORS=(
	"$BASE_URL"
	"https://download.fastgit.org/gohugoio/hugo/releases/download/${VERSION}/${ASSET}"
	"https://mirror.ghproxy.com/${BASE_URL}"
)

TMP=$(mktemp -d)
SUCCESS=0
for URL in "${MIRRORS[@]}"; do
	echo "Attempting download: $URL" >&2
	if curl -L --fail --connect-timeout 15 --retry 2 "$URL" -o "$TMP/hugo.tgz"; then
		SUCCESS=1
		break
	else
		echo "Download failed from: $URL" >&2
	fi
done

if [[ $SUCCESS -ne 1 ]]; then
	echo "All download attempts failed." >&2
	exit 1
fi

tar -xzf "$TMP/hugo.tgz" -C "$TMP" hugo
mkdir -p vendor/hugo-bin
mv "$TMP/hugo" vendor/hugo-bin/hugo
chmod +x vendor/hugo-bin/hugo
echo "Hugo downloaded: $(vendor/hugo-bin/hugo version | head -n1)"
exit 0