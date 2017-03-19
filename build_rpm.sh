#!/bin/bash -xe

COMMIT_ID=$(git show-ref --hash refs/heads/master)
SHORT_COMMIT_ID=$(git show-ref --hash=7 refs/heads/master)
TAR_FILE=protobuf-$COMMIT_ID.tar.gz

git archive --format=tar --prefix="protobuf/" $COMMIT_ID | gzip > $TAR_FILE
rpmbuild -tb --define "COMMIT_ID $COMMIT_ID" ./$TAR_FILE

cp /usr/src/rpm/RPMS/x86_64/protobuf-*$SHORT_COMMIT_ID.*.rpm .
cp /usr/src/rpm/RPMS/x86_64/protobuf-compiler-*$SHORT_COMMIT_ID.*.rpm .
cp /usr/src/rpm/RPMS/x86_64/protobuf-devel-*$SHORT_COMMIT_ID.*.rpm .
