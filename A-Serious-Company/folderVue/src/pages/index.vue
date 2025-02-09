<template>
  
  <v-container>
    <v-row>
      <v-col cols="12">
        <h1>Folder Management System</h1>
      </v-col>
      <v-col>
        <v-btn color="primary" @click="addFolder">Add New Folder</v-btn>
      </v-col>
    </v-row>

    <v-row>
      <v-col
        v-for="folder in folders"
        :key="folder.id"
        cols="12"
        sm="6"
        md="4"
        lg="3"
      >
        <FolderCard :folder="folder" @edit="editFolder" @delete="deleteFolder" />
      </v-col>
    </v-row>

    <FolderDialog
      v-if="dialog"
      :modelValue="dialog"
      :title="dialogTitle"
      :folder="editedFolder"
      @save="saveFolder"
      @close="closeDialog"
    />
  </v-container>
</template>

<script>
import { useFolderStore } from "../stores/folderStore";

export default {
  setup() {
    const folderStore = useFolderStore();
    const folders = ref([]);
    const dialog = ref(false);
    const dialogTitle = ref("Add New Folder");
    const editedFolder = ref({ title: "" });

    onMounted(async () => {
      folders.value = await folderStore.fetchFolders();
    });

    const addFolder = () => {
      dialogTitle.value = "Add New Folder";
      editedFolder.value = { title: "" };
      dialog.value = true;
    };

    const editFolder = (folder) => {
      dialogTitle.value = "Edit Folder";
      editedFolder.value = { ...folder };
      dialog.value = true;
    };

    const saveFolder = async (folder) => {
      await folderStore.saveFolder(folder);
      folders.value = await folderStore.fetchFolders();
      dialog.value = false;
    };

    const deleteFolder = async (folderId) => {
      await folderStore.deleteFolder(folderId);
      folders.value = await folderStore.fetchFolders();
    };

    const closeDialog = () => {
      dialog.value = false;
    };

    return {
      folders,
      dialog,
      dialogTitle,
      editedFolder,
      addFolder,
      editFolder,
      saveFolder,
      deleteFolder,
      closeDialog,
    };
  },
};
</script>