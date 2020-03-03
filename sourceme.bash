
function gpython3 {
    docker run --rm -v$PWD:/data -w /data sjkillen/python3-graphviz $@
}
