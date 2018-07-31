package org.parcore.domain;

import com.google.gson.annotations.SerializedName;
import io.swagger.annotations.ApiModel;
import io.swagger.annotations.ApiModelProperty;

import java.util.ArrayList;
import java.util.List;
import java.util.Objects;

@ApiModel(description = "A list of tools")
public class Tools {

    @SerializedName("tools")
    private List<Tool> tools = null;

    public void addTool(Tool tool) {
        if (this.tools == null) {
            this.tools = new ArrayList<>();
        }
        this.tools.add(tool);
    }

    /**
     * Get tools
     *
     * @return tools
     **/
    @ApiModelProperty(value = "")
    public List<Tool> getTools() {
        if (this.tools == null) {
            this.tools = new ArrayList<>();
        }
        return tools;
    }

    public void setTools(List<Tool> tools) {
        this.tools = tools;
    }


    @Override
    public boolean equals(java.lang.Object o) {
        if (this == o) {
            return true;
        }
        if (o == null || getClass() != o.getClass()) {
            return false;
        }
        Tools tools = (Tools) o;
        return Objects.equals(this.tools, tools.tools);
    }

    @Override
    public int hashCode() {
        return Objects.hash(tools);
    }


    @Override
    public String toString() {
        StringBuilder sb = new StringBuilder();
        sb.append("class Tools {\n");

        sb.append("    tools: ").append(toIndentedString(tools)).append("\n");
        sb.append("}");
        return sb.toString();
    }

    /**
     * Convert the given object to string with each line indented by 4 spaces
     * (except the first line).
     */
    private String toIndentedString(java.lang.Object o) {
        if (o == null) {
            return "null";
        }
        return o.toString().replace("\n", "\n    ");
    }

}
