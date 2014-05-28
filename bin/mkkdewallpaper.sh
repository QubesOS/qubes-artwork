#!/bin/sh

# The Qubes OS Project, http://www.qubes-os.org
#
# Copyright (C) 2014  Wojciech Porczyk <wojciech@porczyk.eu>
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.

BASE="${1}"
SRC="${2}"
AUTHOR="${3}"
LICENCE="${4}"

shift 4
# now $@ contains geometries

DST="$(basename "${SRC}" .svg | sed -e 's/-/_/g' -e 's/[^ _]*/\u&/g')"
NAME="$(echo "${DST}" | sed -e 's/_/ /g')"
DST="${BASE}/${DST}"

echo "creating KDE wallpaper plugin: ${NAME}" >&2

mkdir -p "${DST}"
cat >"${DST}"/metadata.desktop <<EOF
[Desktop Entry]
Name=${NAME}
X-KDE-PluginInfo-Name=${NAME}
X-KDE-PluginInfo-Author=${AUTHOR}
X-KDE-PluginInfo-License=${LICENCE}
EOF

mkdir -p "${DST}"/contents
convert "${SRC}" -geometry x250 "${DST}"/contents/screenschot.png

mkdir -p "${DST}"/contents/images
for geometry in "$@"; do
	echo "  resizing to ${geometry}" >&2
	convert "${SRC}" -geometry "${geometry}" "${DST}"/contents/images/"${geometry}".png
done
