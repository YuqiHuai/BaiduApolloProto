
function build_py_proto() {
  if [ -d "./py_proto" ];then
    rm -rf py_proto
  fi
  mkdir py_proto

  target_directory=""

  if [ -d "modules/common_msgs/" ];then
    target_directory="modules/common_msgs/"
  else
    target_directory="modules/"
  fi

  find "$target_directory" -name "*.proto" \
      | grep -v node_modules \
      | xargs protoc --python_out=py_proto

  find "$target_directory" -name "*.proto" \
      | grep -v node_modules \
      | xargs protol --create-package --in-place --python-out=py_proto protoc --proto-path=$(pwd)
}

build_py_proto